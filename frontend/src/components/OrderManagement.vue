<template>
    <v-text-field
        v-model="search"
        label="搜索订单"
        append-icon="mdi-magnify"
        single-line
        hide-details
    ></v-text-field>
    <v-data-table-server
        v-model="selected"
        :headers="headers"
        :items="paginatedItems"
        :items-length="filteredItems.length"
		item-value="order_id"
        hide-default-footer
        show-select
    >
    </v-data-table-server>
    <v-pagination
        v-model="page"
        :length="pageCount"
        :total-visible="7"
        color="primary"
    ></v-pagination>
</template>

<script setup>
import { ref, computed } from 'vue';

const headers = [
    { title: '订单号', value: 'order_id', sortable: true },
    { title: '用户编号', value: 'customer_id', sortable: true },
    { title: '总价', value: 'price', sortable: true },
    { title: '状态', value: 'status', sortable: true },
];

const items = ref([
    { order_id: 1, customer_id: 1, price: 100, status: '已支付' },
    { order_id: 2, customer_id: 2, price: 200, status: '未支付' },
    { order_id: 3, customer_id: 3, price: 300, status: '已支付' },
    { order_id: 4, customer_id: 4, price: 400, status: '未支付' },
    { order_id: 5, customer_id: 5, price: 500, status: '已支付' },
]);

const search = ref('');
const page = ref(1);
const itemsPerPage = 10;

const filteredItems = computed(() => {
    const lowerSearch = search.value.toLowerCase();
    return items.value.filter(item =>
        Object.values(item).some(val =>
            String(val).toLowerCase().includes(lowerSearch)
        )
    );
});

const paginatedItems = computed(() => {
    const start = (page.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return filteredItems.value.slice(start, end);
});

const pageCount = computed(() => Math.ceil(filteredItems.value.length / itemsPerPage));

const selected = ref([]);
</script>