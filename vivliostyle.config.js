module.exports = {
  title: 'タイトル', // populated into 'publication.json', default to 'title' of the first entry or 'name' in 'package.json'.
  author: '著者名', // default to 'author' in 'package.json' or undefined
  // language: 'jp',
  // size: 'A6',
  entry: [ // **required field**

    {
      title: `前書`,
      path: 'scripts/foreword.md',
      theme: 'resources/layout_foreword.css'
    },

    {
      title: `本文`,
      path: 'output/body_preformatted.md',
      theme: 'resources/layout_body.css'
    },

    {
      title: `奥付`,
      path: 'scripts/colophon.md',
      theme: 'resources/layout_colophon.css'
    },

    // 'introduction.md', // 'title' is automatically guessed from the file (frontmatter > first heading)
    // {
    //   path: 'epigraph.md',
    //   title: 'おわりに', // title can be overwritten (entry > file),
    //   theme: '@vivliostyle/theme-whatever' // theme can be set indivisually. default to root 'theme'
    // },
    // 'glossary.html' // html is also acceptable
  ], // 'entry' can be 'string' or 'object' if there's only single markdown file
  // entryContext: './manuscripts', // default to '.' (relative to 'vivliostyle.config.js')
  // output: [ // path to generate draft file(s). default to '{title}.pdf'
  //   './output.pdf', // the output format will be inferred from the name.
  //   {
  //     path: './book',
  //     format: 'webpub',
  //   },
  // ],
  // workspaceDir: '.vivliostyle', // directory which is saved intermediate files.
  // toc: true, // whether generate and include ToC HTML or not, default to 'false'.
  // cover: './cover.png', // cover image. default to undefined.
  // vfm: { // options of VFM processor
  //   hardLineBreaks: true, // converts line breaks of VFM to <br> tags. default to 'false'.
  //   disableFormatHtml: true, // disables HTML formatting. default to 'false'.
  // },
};
