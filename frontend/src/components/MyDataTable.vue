<template>
	<v-data-table :headers="props.headers" :items="items" :sort-by="[{ key: 'id', order: 'asc' }]">
		<template v-slot:top>
			<v-toolbar flat>
				<v-toolbar-title>{{ props.title }}</v-toolbar-title>
				<v-divider class="mx-4" inset vertical></v-divider>
				<v-spacer></v-spacer>
				<v-dialog v-model="dialog" max-width="500px">
					<template v-slot:activator="{ props }">
						<v-btn class="mb-2" color="primary" dark v-bind="props">
							添加
						</v-btn>
					</template>
					<v-card>
						<v-card-title>
							<span class="text-h5">{{ formTitle }}</span>
						</v-card-title>

						<v-card-text>
							<v-container>
								<v-row>
									<v-col v-for="header in headers.slice(0, -1)" :key="header.value" cols="12">
										<v-text-field v-if="header.type === 'number'"
											v-model="editedItem[header.value]" :label="header.title"></v-text-field>
										<v-textarea v-if="header.type === 'string'" v-model="editedItem[header.value]"
											:label="header.title"></v-textarea>
										<v-file-input v-if="header.type === 'image'" v-model="editedItem[header.value]"
											:label="header.title" prepend-icon="mdi-camera" variant="filled"></v-file-input>
									</v-col>
								</v-row>
							</v-container>
						</v-card-text>

						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn color="blue-darken-1" variant="text" @click="close">
								取消
							</v-btn>
							<v-btn color="blue-darken-1" variant="text" @click="save">
								保存
							</v-btn>
						</v-card-actions>
					</v-card>
				</v-dialog>
				<v-dialog v-model="dialogDelete" max-width="500px">
					<v-card>
						<v-card-title class="text-h5">是否确定删除这一项?</v-card-title>
						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn color="blue-darken-1" variant="text" @click="closeDelete">取消</v-btn>
							<v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">确定</v-btn>
							<v-spacer></v-spacer>
						</v-card-actions>
					</v-card>
				</v-dialog>
			</v-toolbar>
		</template>
		<template v-slot:[`item.actions`]="{ item }">
			<v-icon class="me-2" size="small" @click="editItem(item)">
				mdi-pencil
			</v-icon>
			<v-icon size="small" @click="deleteItem(item)">
				mdi-delete
			</v-icon>
		</template>
		<template v-slot:no-data>
			<v-sheet color="primary">
				<v-card-text class="white--text">
					没有找到数据，请添加一些数据。
				</v-card-text>
			</v-sheet>
		</template>
	</v-data-table>
</template>
<script setup>
import { ref, computed, nextTick, onMounted, watch } from 'vue'
import { defineProps } from 'vue';
const dialog = ref(false)
const dialogDelete = ref(false)
const props = defineProps({
	headers: Array,
	title: String,
	items: Object,
	defaultItem: Object,
	addItem: Function,
	updateItem: Function,
	deleteItem: Function,
});
const items = ref([]);
// 使用 onMounted 钩子在组件挂载时初始化 items
onMounted(() => {
	items.value = props.items;
	console.log('Items initialized:', items.value);
});

// 监听 props.items 的变化，并更新 items
watch(() => props.items, (newItems) => {
	items.value = newItems;
	console.log('Items updated:', items.value);
});


const editedIndex = ref(-1);
const editedItem = ref({ ...props.defaultItem });
const defaultItem = ref({ ...props.defaultItem });

const formTitle = computed(() => {
	return editedIndex.value === -1 ? '添加' : '修改';
});

const editItem = (item) => {
	editedIndex.value = items.value.indexOf(item)
	editedItem.value = Object.assign({}, item)
	dialog.value = true
}

const deleteItem = (item) => {
	editedIndex.value = items.value.indexOf(item)
	editedItem.value = Object.assign({}, item)
	dialogDelete.value = true
}

const deleteItemConfirm = () => {
	console.log(editedIndex.value)
	items.value.splice(editedIndex.value, 1)
	props.deleteItem(editedItem.value)
	closeDelete()
}

const close = () => {
	dialog.value = false
	nextTick(() => {
		editedItem.value = Object.assign({}, defaultItem)
		editedIndex.value = -1
	})
}

const closeDelete = () => {
	dialogDelete.value = false
	nextTick(() => {
		editedItem.value = Object.assign({}, defaultItem)
		editedIndex.value = -1
	})
}

const save = () => {
	if (editedIndex.value > -1) {
		Object.assign(items.value[editedIndex.value], editedItem.value)
		props.updateItem(editedItem.value)
	} else {
		items.value.push(editedItem.value)
		props.addItem(editedItem.value)
	}
	close()
}
</script>
<script>
export default {

	watch: {
		dialog(val) {
			val || this.close()
		},
		dialogDelete(val) {
			val || this.closeDelete()
		},
	},
}
</script>