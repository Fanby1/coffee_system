<template>
	<main-layout>
		<template v-slot:toolbar-icons>
			<cart-dialog></cart-dialog>
			<v-btn icon>
				<v-icon>mdi-magnify</v-icon>
			</v-btn>
			<v-btn icon>
				<v-icon>mdi-heart</v-icon>
			</v-btn>
			<v-btn icon>
				<v-icon>mdi-dots-vertical</v-icon>
			</v-btn>
		</template>
		<template v-slot:main>
			<v-container class="pa-0" fluid>
				<coffee-carousel></coffee-carousel>
				<template v-slot:image>
					<v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"></v-img>
				</template>
				<coffee-display-area></coffee-display-area>
			</v-container>
		</template>
	</main-layout>
</template>

<script setup>
import MainLayout from '@/components/MainLayout.vue';
import CoffeeCarousel from '@/components/CoffeeCarousel.vue';
import CoffeeDisplayArea from '@/components/CoffeeDisplayArea.vue';
import CartDialog from '@/components/CartDialog.vue';
</script>

<style scoped>
.main-background {
	background-color: #f5f5f5;
	/* 设置你想要的背景颜色 */
}
</style>