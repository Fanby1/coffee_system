<template>
	<v-card class="mx-auto" max-width="344">
		<v-img height="200px" :src=image cover></v-img>

		<v-card-title>
			{{ name }}
		</v-card-title>

		<v-card-subtitle>
			{{ price }}
		</v-card-subtitle>

		<v-card-actions>
			<v-btn color="orange-lighten-2" text="Explore"></v-btn>

			<v-spacer></v-spacer>

			<v-btn :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show"></v-btn>
		</v-card-actions>

		<v-expand-transition>
			<div v-show="show">
				<v-divider></v-divider>

				<v-card-text>
					{{ discribe }}
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
		image: {
			type: String,
			required: true
		},
		name: {
			type: String,
			required: true
		},
		price: {
			type: String,
			required: true
		},
		discribe: {
			type: String,
			required: true
		}
	},
	setup() {
        const show = ref(false);
        return { show };
    }
}
</script>

<style scoped>
.v-card {
	max-width: 400px;
	margin: 20px;
}
</style>