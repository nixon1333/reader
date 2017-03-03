module.exports = {
    entry: "./app/app.js",
    output: {
        path: "./dist/js/",
        filename: "bundle.js",
        sourceMapFilename: "bundle.js.map",
    },

    watch: true,
    //
    // // eslint config
    // // eslint: {
    // //   configFile: './config/eslint.json'
    // // },
    //
    // module: {
    //     loaders: [
    //       { test: /\.css$/, loader: "style!css" },
    //       { test: /\.html$/, loader: "mustache-loader" },
    //       { test: /\.json$/, loader: "json-loader" }]
    // },
    //
    // resolve: {
    //     extensions: ['', '.js']
    // }
};