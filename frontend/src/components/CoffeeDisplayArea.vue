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
                    :image="coffee.image"
                    :name="coffee.name"
                    :price="coffee.price"
                ></coffee-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import CoffeeCard from './CoffeeCard.vue';

export default {
    name: 'CoffeeList',
    components: {
        CoffeeCard
    },
    setup() {
        const coffees = ref([]);

        const fetchCoffees = async () => {
            try {
                const response = await axios.get('/api/coffees');
                coffees.value = response.data.coffees;
				console.log(coffees.value);
            } catch (error) {
                console.error('Error fetching coffee data:', error);
            }
        };

        onMounted(() => {
            fetchCoffees();
        });

        return {
            coffees
        };
    }
};
</script>

<style scoped>
.v-container {
    margin-top: 20px;
}
</style>