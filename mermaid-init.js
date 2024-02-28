mermaid.initialize({
    startOnLoad: true,
    securityLevel: 'loose',
    theme: 'neutral',
    themeVariables: {
        // 'primaryColor': '#282828', // Gruvbox dark background
        // 'primaryTextColor': '#ebdbb2', // Gruvbox light background
        // 'primaryBorderColor': '#3c3836', // Gruvbox dark gray
        // 'lineColor': '#d5c4a1', // Gruvbox light yellow
        // 'secondaryColor': '#32302f', // Gruvbox darker gray
        // 'tertiaryColor': '#ebdbb2', // Gruvbox light background
        // 'background': '#282828', // Gruvbox dark background for diagrams
        // 'mainBkg': '#282828', // Gruvbox dark background for main elements
        // 'errorBkgColor': '#fb4934', // Gruvbox red for errors
        // 'errorTextColor': '#282828', // Gruvbox dark background for error text
        // 'noteBkgColor': '#32302f', // Gruvbox darker gray for notes
        // 'noteTextColor': '#ebdbb2', // Gruvbox light background for note text
        // 'noteBorderColor': '#3c3836', // Gruvbox dark gray for note borders
        // 'textColor': '#ebdbb2', // Gruvbox light background for text
        // 'border1Color': '#3c3836', // Gruvbox dark gray for borders
        // 'border2Color': '#d5c4a1', // Gruvbox light yellow for secondary borders
        // 'border3Color': '#282828', // Gruvbox dark background for tertiary borders
        // 'border4Color': '#fb4934', // Gruvbox red for error borders
        // 'border5Color': '#32302f' // Gruvbox darker gray for quinary borders
    },
    flowchart: {
        nodeSpacing: 100,
        rankSpacing: 100,
        curve: "linear",
        subGraphTitleMargin: {
            top: 10,
            bottom: 10
        },
        defaultRenderer: 'elk'
    }
});
