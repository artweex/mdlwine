<template>
	<v-card
		class="elevation-2"
		:to="url"
	>
		<v-img
			height="200"
			:src="item.images"
		></v-img>

		<v-card-title style="font-size: 1rem">
			{{ item.title }}
		</v-card-title>

	</v-card>
</template>

<script lang="coffee">

export default {
	name: "product-card"
	props:
		item:
			type: Object
			required: true

	computed:
		url: -> "/product/#{@item.slug}"
}
</script>