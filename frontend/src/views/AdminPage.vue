<template>
	<main-layout>
		<template v-slot:toolbar-icons></template>
		<template v-slot:main>
			<v-sheet class="fill-height">
				<v-navigation-drawer>
					<v-list dense>
						<v-list-item v-for="item in items" :key="item.value"
							:class="{ 'deep-purple--text text--accent-4': selectedTab === item.value }"
							@click="selectedTab = item.value">
							<v-row align="center">
								<v-col cols="auto">
									<v-icon>{{ item.icon }}</v-icon>
								</v-col>
								<v-col>
									<v-list-item-title>{{ item.title }}</v-list-item-title>
								</v-col>
							</v-row>
						</v-list-item>
					</v-list>
				</v-navigation-drawer>

				<v-sheet>
					<product-management v-if="selectedTab == 'products'" />
					<order-management v-if="selectedTab == 'orders'" />
				</v-sheet>
			</v-sheet>
		</template>
	</main-layout>
</template>

<script setup>
import { ref } from 'vue';
import MainLayout from '@/components/MainLayout.vue';
import ProductManagement from '@/components/ProductManagement.vue';
import OrderManagement from '@/components/OrderManagement.vue';

const selectedTab = ref('products');
const items = ref([
	{ value: 'products', icon: 'mdi-cube-outline', title: '产品管理' },
	{ value: 'orders', icon: 'mdi-receipt', title: '订单管理' },
]);
</script>

<style scoped>
.fill-height {
	height: 100%;
}
</style>