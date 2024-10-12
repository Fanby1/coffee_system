<template>
	<v-app>
		<v-navigation-drawer app>
			<!-- 侧边栏内容 -->
			<v-list>
				<v-list-item>
					<v-list-item-content>
						<v-list-item-title>菜单项1</v-list-item-title>
					</v-list-item-content>
				</v-list-item>
				<v-list-item>
					<v-list-item-content>
						<v-list-item-title>菜单项2</v-list-item-title>
					</v-list-item-content>
				</v-list-item>
			</v-list>
		</v-navigation-drawer>

		<v-app-bar app>
			<!-- 顶部导航栏内容 -->
			<v-toolbar-title>我的咖啡点单系统</v-toolbar-title>
		</v-app-bar>

		<v-main>
			<!-- 主内容 -->
			<v-container>
				<router-view></router-view>
			</v-container>
		</v-main>
	</v-app>
</template>

<script>
export default {
	name: "ModernLayout",
};
</script>

<style>
/* 你可以在这里添加自定义样式 */
</style>