<template>
	<v-card class="mx-auto" max-width="344">
		<v-img height="200px" :src=item.image cover></v-img>

		<v-card-title>
			{{ item.name }}
		</v-card-title>
		<v-sheet>
			<v-row>
				<v-col cols="4" class="text-center">
					Price: ${{ item.price }}
				</v-col>

				<v-col cols="8" class="text-center">
					<!-- 增加和减少数量按钮 -->
					<v-btn icon @click="decreaseItemQuantity(item.id)" :disabled="getQuantity(item.id) <= 0">
						<v-icon>mdi-minus</v-icon>
					</v-btn>
					<span class="mx-2">{{ getQuantity(item.id) }}</span>
					<v-btn icon @click="increaseItemQuantity(item.id)">
						<v-icon>mdi-plus</v-icon>
					</v-btn>
				</v-col>
			</v-row>
		</v-sheet>

		<v-card-actions>
			<v-btn color="orange-lighten-2" text="Explore"></v-btn>

			<v-spacer></v-spacer>

			<v-btn :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show"></v-btn>
		</v-card-actions>

		<v-expand-transition>
			<div v-show="show">
				<v-divider></v-divider>

				<v-card-text>
					{{ item.discribe }}
				</v-card-text>
			</div>
		</v-expand-transition>
	</v-card>
</template>

<script>
import { ref } from 'vue';

export default {
	name: 'CoffeeCard',
	props: {
		item: {
			type: Object,
			required: true
		}
	},
}
</script>

<script setup>
import { useStore } from 'vuex';

const store = useStore();
const show = ref(false);

// 处理增加和减少商品数量的逻辑
const increaseItemQuantity = (itemId) => {
	store.commit('increaseItemQuantity', itemId);
};

const decreaseItemQuantity = (itemId) => {
	store.commit('decreaseItemQuantity', itemId);
};
const getQuantity = (itemId) => store.getters.getQuantityById(itemId);

</script>

<style scoped>
.v-card {
	max-width: 400px;
	margin: 20px;
}
</style>