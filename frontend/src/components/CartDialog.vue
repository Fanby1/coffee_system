<template>
	<v-dialog max-width="5000">
		<template v-slot:activator="{ props: activatorProps }">
			<v-badge v-if="cartItemsCount > 0" color="red" :content="cartItemsCount" v-bind="activatorProps" overlap>
				<v-btn icon>
					<v-icon>mdi-cart</v-icon> <!-- Vuetify 自带购物车图标 -->
				</v-btn>
			</v-badge>

			<v-btn v-else icon v-bind:="activatorProps">
				<v-icon>mdi-cart</v-icon>
			</v-btn>
		</template>

		<template v-slot:default="{ isActive }">

			<v-container>
			<v-card>
				<v-toolbar>
					<v-toolbar-title>购物车</v-toolbar-title>
					<v-spacer></v-spacer>
					<!-- 显示购物车总价格 -->
					Total: {{ totalPrice }}
					<v-btn icon @click="isActive.value = false">
						<v-icon>mdi-close</v-icon>
					</v-btn>
				</v-toolbar>

				<v-row>
					<v-col cols="12">
						<!-- 购物车内容部分，设定固定高度以实现滚动 -->
						<v-list class="shopping-cart" max-height="400" style="overflow-y: auto;">
							<v-list-item v-for="(item, ) in cartItems" :key="item.id">
								<v-card class="pa-4 mb-3">
									<v-row>
										<v-col cols="6">
											<h4>{{ item.name }}</h4>
											<p>Price: ${{ item.price }}</p>
										</v-col>

										<v-col cols="6" class="text-right">
											<!-- 增加和减少数量按钮 -->
											<v-btn icon @click="decreaseItemQuantity(item.id)"
												:disabled="item.quantity <= 0">
												<v-icon>mdi-minus</v-icon>
											</v-btn>
											<span class="mx-2">{{ item.quantity }}</span>
											<v-btn icon @click="increaseItemQuantity(item.id)">
												<v-icon>mdi-plus</v-icon>
											</v-btn>
										</v-col>
									</v-row>
								</v-card>
							</v-list-item>
						</v-list>
					</v-col>
				</v-row>

			</v-card>
			</v-container>
		</template>
	</v-dialog>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();

// 获取购物车中的商品列表和总价格
const cartItems = computed(() => store.getters.cartItems);
const totalPrice = computed(() => store.getters.totalPrice);
const cartItemsCount = computed(() => store.getters.cartItemsCount);

// 处理增加和减少商品数量的逻辑
const increaseItemQuantity = (itemId) => {
	store.commit('increaseItemQuantity', itemId);
};

const decreaseItemQuantity = (itemId) => {
	store.commit('decreaseItemQuantity', itemId);
};
</script>

<style scoped>
.shopping-cart {
	max-height: 400px;
	/* 固定高度 */
	overflow-y: auto;
	/* 启用垂直滚动 */
}
</style>