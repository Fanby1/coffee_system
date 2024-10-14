const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000", // 后端 API 地址
        changeOrigin: true, // 允许跨域
		pathRewrite: { '^/api': '' },
      },
	  '/static': {
        target: 'http://localhost:5000', // 将静态文件代理到 Flask 的服务器
        changeOrigin: true               // 确保跨域问题被处理
      },
    },
  },

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  }
});
