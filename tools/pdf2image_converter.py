import argparse

from glob import glob
from os import write
from tqdm import tqdm
from shutil import copy
from tempfile import TemporaryDirectory
from pdf2image import pdfinfo_from_path, convert_from_path
from img2pdf import convert as convert_img2pdf
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

def merge2pdfs(src1, src2, dst):
    with (open(src1, "rb") as pdf1, open(src2, "rb") as pdf2, open(dst, "wb") as out):
         merger = PdfFileMerger()
         merger.append(pdf1)
         merger.append(pdf2)
         merger.write(out)
         merger.close()

def main():
    # # 一時的にPATHを追加
    # poppler_dir = os.getcwd() + "/poppler-0.68.0/bin"
    # os.environ["PATH"] = poppler_dir
    args = parser.parse_args()
    dpi = args.dpi
    split_width = args.split_width

    # PDFの画像化
    
    target_pdf = args.input
    info = pdfinfo_from_path(target_pdf, userpw=None, poppler_path=None)
    
    maxPages = info["Pages"]
    with TemporaryDirectory() as tempDir:
        idx = 0
        for page in tqdm(range(1, maxPages+1, split_width)): 
            print("loading pdf...")
            pages = convert_from_path(target_pdf, dpi=dpi, first_page=page, last_page=min(page+split_width-1,maxPages), output_folder=tempDir) # dpiの指定
            print("export images...")
            for i, p in enumerate(tqdm(pages, leave=False)):
                p.save(tempDir + f"/image_{i:02}.png", dpi=(dpi, dpi)) # dpiの指定とTIFFの圧縮
            print("save temporary pdf...")
            images = sorted(glob(tempDir + '/*.' + 'png'))
            with open(tempDir + f"/output_{idx:06}.pdf", "wb") as pdf:
                pdf.write(convert_img2pdf(images))
            idx += 1
            print("\033[3A", end="") # 3行分の出力を消す

        print("merge temporary pdfs...")
        pdfs = sorted(glob(tempDir + '/*.' + 'pdf'))

        writer = PdfFileWriter()
        for i, pdf in enumerate(pdfs):
            reader = PdfFileReader(pdf)
            for j in range(reader.getNumPages()):
                writer.addPage(reader.getPage(j))
        with open('out2.pdf', mode='wb') as f:
            writer.write(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="target.pdf")
    parser.add_argument("-o", "--output", default="output.pdf")
    parser.add_argument("--dpi", default=1200)
    parser.add_argument("--split_width", default=10)
    main()