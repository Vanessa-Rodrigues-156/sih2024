const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
module.exports = {
  publicPath: './', // Use relative paths for assets in Electron
  outputDir: 'dist', // Ensure output is directed to 'dist'
};
