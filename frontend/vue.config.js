const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000", // 后端 API 地址
        changeOrigin: true, // 允许跨域
      },
    },
  },
});
