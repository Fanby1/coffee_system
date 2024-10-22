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
								<v-text-field v-model="username.value.value" :counter="10"
									:error-messages="username.errorMessage.value" label="用户名"></v-text-field>

								<v-text-field v-model="phone.value.value" :counter="7"
									:error-messages="phone.errorMessage.value" label="电话"></v-text-field>

								<v-text-field v-model="email.value.value" :error-messages="email.errorMessage.value"
									label="邮箱"></v-text-field>

								<v-text-field v-model="password.value.value" :error-messages="password.errorMessage.value"
									label="密码"></v-text-field>

								<v-checkbox v-model="checkbox.value.value" :error-messages="checkbox.errorMessage.value"
									label="同意用户协议(没编出来)" type="checkbox" value="1"></v-checkbox>

								<v-btn class="me-4" type="submit">
									注册
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
import { useField, useForm } from 'vee-validate'
import { useRouter } from 'vue-router';
import axios from 'axios'

const { handleSubmit, handleReset } = useForm({
	validationSchema: {
		username(value) {
			if (value?.length >= 2) return true

			return '请输入合法的用户名'
		},
		phone(value) {
			if (/^[0-9-]{7,}$/.test(value)) return true

			return '请输入合法的电话号码'
		},
		email(value) {
			if (/^[0-9a-z.-]+@[0-9a-z.-]+\.[a-z]+$/i.test(value)) return true

			return '请输入合法的邮箱'
		},
		password(value) {
			if (value?.length >= 6) return true

			return '请输入合法的密码'
		},
		checkbox(value) {
			if (value === '1') return true

			return '必须选择同意用户协议.'
		},
	},
})
const username = useField('username')
const phone = useField('phone')
const email = useField('email')
const password = useField('password')
const checkbox = useField('checkbox')

const router = useRouter();

const submit = handleSubmit(async values => {
	const response = await axios.post('api/register', values);

	if (response.data.message === "Register failed"){
		alert("注册失败");
		return;
	}
	alert("注册成功 请登录系统");

    router.push({path : '/log-in'});
})
</script>

<script>
import AuthenticationLayout from '@/components/AuthenticationLayout.vue';
export default {
	name: 'sign-up',
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
}
</style>