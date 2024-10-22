<template>
    <v-container>
        <v-row>
            <v-col
                v-for="coffee in coffees"
                :key="coffee.name"
                cols="12"
                md="4"
            >
                <coffee-card
                    :item = "coffee"
                ></coffee-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { useStore } from 'vuex';
import { computed, onMounted } from 'vue';
import CoffeeCard from './CoffeeCard.vue';
const store = useStore();

onMounted(() => {
  store.dispatch('fetchAllItems').then(() => {
	console.log("get result")
	console.log(store.getters.shopItems);
  }); // 触发获取购物车数据的 action
});

const coffees = computed(() => store.getters.shopItems);
</script>

<style scoped>
.v-container {
    margin-top: 20px;
}
</style>