<template>
	<v-layout>
		<v-app-bar scroll-behavior="hide collapse elevate fade-image" color="teal-darken-4"
			image="https://picsum.photos/1920/1080?random">
			<template v-slot:image>
				<v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"></v-img>
			</template>

			<template v-slot:prepend>
				<v-app-bar-nav-icon />
			</template>

			<v-card>
				<v-img :src="require('/src/assets/language-java.png')" height="40px" width="40px"></v-img>
			</v-card>
			<v-app-bar-title>好喝的咖啡店</v-app-bar-title>

			<v-spacer></v-spacer>

			<v-btn icon>
				<v-icon>mdi-magnify</v-icon>
			</v-btn>

			<v-btn icon>
				<v-icon>mdi-heart</v-icon>
			</v-btn>

			<v-btn icon>
				<v-icon>mdi-dots-vertical</v-icon>
			</v-btn>
			<v-card color="primary" class="mr-2">
				<v-btn @click="login">
					登录
				</v-btn>
			</v-card>
			<v-card color="secondary" class="mr-5">
				<v-btn @click="register">
					注册
				</v-btn>
			</v-card>
		</v-app-bar>

		<v-main class="main-background">
			<v-container class="pa-0" fluid>
				<coffee-carousel></coffee-carousel>
				<template v-slot:image>
					<v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"></v-img>
				</template>
				<coffee-display-area></coffee-display-area>
			</v-container>
		</v-main>
	</v-layout>
</template>

<script>
import CoffeeDisplayArea from './CoffeeDisplayArea.vue';
import CoffeeCarousel from './CoffeeCarousel.vue';

export default {
	data: () => ({
		order: 0,
	}),
	components: {
		CoffeeDisplayArea, CoffeeCarousel
	}, 
	methods: {
		login() {
			// 登录逻辑
			alert('登录按钮被点击');
		},
		register() {
			// 注册逻辑
			alert('注册按钮被点击');
		}
	}
}
</script>

<style scoped>

.main-background {
    background-color: #f5f5f5; /* 设置你想要的背景颜色 */
}
</style>