<template>
	<v-bottom-navigation
		grow
		color="red darken-4"
		app
	>
		<v-btn
			v-for="(item, index) in menu"
			:key="index"
			:to="item.link"
		>
			<span>{{ item.title }}</span>
			<v-icon>{{ item.icon }}</v-icon>
		</v-btn>
	</v-bottom-navigation>
</template>

<script lang="coffee">
export default {
	data: ->
		return {
			activeBtn: 1,
			menu: [
				{
					title: 'About'
					icon: 'mdi-home'
					link: '/'
				}
				{
					title: 'Products'
					icon: 'mdi-shopping'
					link: '/products'
				}
				{
					title: 'Feedback'
					icon: 'mdi-information-variant'
					link: '/feedback'
				}
			]
		}

}
</script>