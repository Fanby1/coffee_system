<template>
	<my-data-table :title="title" :headers="headers" :items="items" :defaultItem="defaultItem" :updateItem="updateItem"
		:deleteItem="deleteItem" :addItem="addItem"></my-data-table>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import MyDataTable from '@/components/MyDataTable.vue';
import { useStore } from 'vuex';
const store = useStore();
const title = ref('产品管理');

const defaultItem = ref({
	id: 0,
	product_name: '',
	discribe: '',
	price: 0,
	store: 0,
});

const items = ref([]);
const headers = ref([]);

const fetchCoffees = async () => {
	try {
		const token = store.getters.token;
		const response = await fetch('/api/coffees-manager', {
			method: 'GET',
			headers: {
				'Authorization': `Bearer ${token}`,
				'Content-Type': 'application/json',
			},
		});
		const data = await response.json();
		items.value = data.coffees;
	} catch (error) {
		console.error('Error fetching coffees:', error);
	}
};

onMounted(() => {
	fetchCoffees();
});

console.log(items);

const fetchHeaders = async () => {
	try {
		const response = await fetch('/api/coffees-headers');
		const data = await response.json();
		headers.value = data;
	} catch (error) {
		console.error('Error fetching headers:', error);
	}
};

onMounted(() => {
	fetchHeaders();
});
console.log(headers);

const updateItem = (item) => {
	console.log(item);
}

const deleteItem = async (item) => {
	try {
		const token = store.getters.token;
		const response = await fetch('/api/delete-products', {
			method: 'POST',
			headers: {
				'Authorization': `Bearer ${token}`,
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ product_ids: [item.id] }),
		});
		const data = await response.json();
		if (data.error.length > 0) {
			console.error('Error deleting products:', data.error);
		} else {
			console.log('Products deleted successfully');
			fetchCoffees(); // Refresh the items after deletion
		}
	} catch (error) {
		console.error('Error deleting products:', error);
	}
}

const addItem = async (item) => {
  try {
    const token = store.getters.token;
    const formData = new FormData();
    formData.append('name', item['product_name']);
    formData.append('price', item['price']);
    formData.append('description', item['describe']);
    formData.append('quantity', item['stock']);
    
    if (item['image']) {
      formData.append('image', item['image']);
    }
	console.log(formData);

    const response = await fetch('/api/add-product', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        // 'Content-Type': 'multipart/form-data', // 不要手动设置
      },
      body: formData,
    });

    const data = await response.json();
    if (data.error && data.error.length > 0) {
      console.error('Error adding products:', data.error);
    } else {
      console.log('Product added successfully');
      fetchCoffees(); // 刷新数据
    }
  } catch (error) {
    console.error('Error adding product:', error);
  }
};
</script>