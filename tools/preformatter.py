import os
import re
import sys

args = sys.argv

def formatRuby(line):
    line = re.sub(r"(\{)(.+)(\|)(.+)(\})", r"<ruby>\2<rt>\4</rt></ruby>", line)
    return line

def formatRule1(line):
    firstLetter = line[0]
    if firstLetter == "「" or firstLetter == "『" or firstLetter == "≪":
        line = formatRuby(line)
        line = "<p class=\"q\">" + line.rstrip(os.linesep) + "</p>" + os.linesep
    return line

def formatRule2(line):
    if line.rstrip(os.linesep) == "::page_break":
        return "<div class=\"page_break\"></div>" + os.linesep
    return line

def formatRule3(line):
    if line.rstrip(os.linesep) == "::blank_line":
        return "<p><br></p>" + os.linesep
    return line

def formatLetterRule(line):
    newline = ""
    i = 0
    for c in line:
        newline += c
        if c == "！" or c == "？":
            if not (line[i+1] == " " or line[i+1] == "　" or line[i+1] == "！" or line[i+1] == "？" or line[i+1] == "」" or line[i+1] == "』"):
                newline += "　"
        i += 1
    return newline

def formatLine(line):
    if line[0] == "<":
        return line
    line = formatRule1(line)
    line = formatRule2(line)
    line = formatRule3(line)
    line = formatLetterRule(line)
    return line

def main():
    # 引数が3つでないならエラー終了
    if len(args) != 3:
        if len(args) > 3:
            print("too many arguments!")
        else:
            print("few argument, please put target filename")
        return -1

    # ターゲットファイルの親ディレクトリとファイル名をパース
    filepath = args[1]
    dirpath  = os.path.dirname(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    
    # 1行ずつ読み込みながらフォーマットし、結果を格納する
    input = open(filepath, "r")
    formatted_lines = []
    while True:
        line = input.readline()
        if not line: break
        formatted_lines.append(formatLine(line))
    input.close()

    # 書き出す
    output = open(args[2] + os.sep + filename + "_preformatted.md", "w")
    for line in formatted_lines:
        output.write(line)
    output.close()

if __name__ == '__main__':
    main()