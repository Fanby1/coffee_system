<template>
	<v-carousel height="400" show-arrows="hover" cycle hide-delimiter-background>
		<v-carousel-item v-for="(slide, i) in slides" :key="i">
			<v-sheet height="100%" class="container"  :style="backgroundStyle(i)">
				<div class="overlay d-flex fill-height justify-center align-center">
					<div class="text-h2">
						{{ slide }} Slide
					</div>
				</div>
			</v-sheet>
		</v-carousel-item>
	</v-carousel>
</template>
<script>
export default {
	data() {
		return {
			colors: [
				'indigo',
				'warning',
				'pink darken-2',
				'red lighten-1',
				'deep-purple accent-4',
			],
			slides: [
				'First',
				'Second',
				'Third',
				'Fourth',
				'Fifth',
			],
		}
	},
	methods: {
		backgroundStyle(i) {
			return {
				backgroundImage: `url(${require('@/assets/coffee_shop_' + i + '.jpg')})`,
			}
		}
	}
}
</script>

<style scoped>
.overlay {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background: rgba(0, 0, 0, 0.3);
	/* 添加半透明背景以确保文字可见 */
}

.container {
	position: relative;
	width: 100%;
	height: 100%;
	/* 确保容器填满可用空间 */
	overflow: hidden;
	/* 确保图片溢出但不允许box有空间剩余 */
}
</style>