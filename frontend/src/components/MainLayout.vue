<template>
	<v-layout>
		<v-app-bar scroll-behavior="hide collapse elevate fade-image" color="teal-darken-4"
			image="https://picsum.photos/1920/1080?random">
			<template v-slot:image>
				<v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"></v-img>
			</template>

			<template v-slot:prepend>
				<v-app-bar-nav-icon />
			</template>

			<v-card>
				<v-img :src="require('/src/assets/language-java.png')" height="40px" width="40px"></v-img>
			</v-card>
			<v-app-bar-title>好喝的咖啡店</v-app-bar-title>

			<v-spacer></v-spacer>
			
			<slot name="toolbar-icons"></slot>

			<v-card v-if="!isAuthenticated" color="primary" class="mr-2">
				<v-btn @click="login">
					登录
				</v-btn>
			</v-card>
			<v-card v-if="!isAuthenticated" color="secondary" class="mr-5">
				<v-btn @click="register">
					注册
				</v-btn>
			</v-card>
            <v-card v-if="isAuthenticated" color="primary" class="mr-2">
                <v-row align="center" no-gutters>
                    <v-col cols="auto" class="ma-2">
                        <v-avatar>
                            <img :src="require('@/assets/avatar.jpg')" alt="Avatar">
                        </v-avatar>
                    </v-col>
                    <v-col>
                        <v-card-title class="pl-2">{{ user.username }}</v-card-title>
                    </v-col>
                </v-row>
            </v-card>
			<v-card v-if="isAuthenticated" color="secondary" class="mr-2">
				<v-btn @click="logout">
					登出
				</v-btn>
			</v-card>
		</v-app-bar>

		<v-main class="main-background">
			<v-container class="pa-0" fluid>
				<slot name="main"></slot>
			</v-container>
		</v-main>
	</v-layout>
</template>

<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore();
const router = useRouter();

const isAuthenticated = computed(() => store.getters.isAuthenticated);
const user = computed(() => store.getters.user);

const login = () => {
    router.push('/log-in');
};

const register = () => {
    router.push('/sign-up');
};

const logout = () => {
	store.dispatch('logout');
	router.push('/');
};
</script>

<style scoped>
.main-background {
	background-color: #f5f5f5;
	/* 设置你想要的背景颜色 */
}
</style>