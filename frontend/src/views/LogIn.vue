<template>
	<authentication-layout :src="require('/src/assets/coffee_shop_0.jpg')">
		<template v-slot:left>
			<v-container>
				<v-row>
					<v-img :src="require('/src/assets/language-java.svg')" />
				</v-row>
				<v-row>
					<v-col cols="12" sm="10" md="10" offset-md="1">
						<v-card>
							<form @submit.prevent="submit">
								<v-text-field v-model="name.value.value" :counter="10"
									:error-messages="name.errorMessage.value" label="用户名"></v-text-field>

								<v-text-field v-model="phone.value.value" :counter="7"
									:error-messages="phone.errorMessage.value" label="电话"></v-text-field>

								<v-text-field v-model="email.value.value" :error-messages="email.errorMessage.value"
									label="邮箱"></v-text-field>

								<v-select v-model="select.value.value" :error-messages="select.errorMessage.value"
									:items="items" label="身份"></v-select>

								<v-checkbox v-model="checkbox.value.value" :error-messages="checkbox.errorMessage.value"
									label="同意用户协议(没编出来)" type="checkbox" value="1"></v-checkbox>

								<v-btn class="me-4" type="submit">
									登录
								</v-btn>

								<v-btn @click="handleReset">
									清空
								</v-btn>
							</form>
						</v-card>
					</v-col>
				</v-row>
			</v-container>
		</template>
	</authentication-layout>
</template>


<script setup>
import { ref } from 'vue'
import { useField, useForm } from 'vee-validate'

const { handleSubmit, handleReset } = useForm({
	validationSchema: {
		name(value) {
			if (value?.length >= 2) return true

			return 'Name needs to be at least 2 characters.'
		},
		phone(value) {
			if (/^[0-9-]{7,}$/.test(value)) return true

			return 'Phone number needs to be at least 7 digits.'
		},
		email(value) {
			if (/^[a-z.-]+@[a-z.-]+\.[a-z]+$/i.test(value)) return true

			return 'Must be a valid e-mail.'
		},
		select(value) {
			if (value) return true

			return 'Select an item.'
		},
		checkbox(value) {
			if (value === '1') return true

			return 'Must be checked.'
		},
	},
})
const name = useField('name')
const phone = useField('phone')
const email = useField('email')
const select = useField('select')
const checkbox = useField('checkbox')

const items = ref([
	'Item 1',
	'Item 2',
	'Item 3',
	'Item 4',
])

const submit = handleSubmit(values => {
	alert(JSON.stringify(values, null, 2))
})
</script>

<script>
import AuthenticationLayout from '@/components/AuthenticationLayout.vue';
export default {
	name: 'LogIn',
	components: {
		AuthenticationLayout
	}
};
</script>

<style scoped>
.fill-height {
	height: 100%;
}

.upLoad-btn {
	position: relative;
	top: 30%;
	/*偏移*/
	/*transform: translateY(50%);*/
	/*text-align: center;*/
}
</style>