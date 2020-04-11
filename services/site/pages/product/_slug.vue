<template>
	<v-card
		max-width="400"
		class="mx-auto"
	>
		<v-container cols="12">
			<v-row dense>
				<v-col
				>
					<v-card 
						
						dark
					>
						<v-img
							:src="item.images"
							height="45%"
							>
						</v-img>
					</v-card>
					<v-card-subtitle >Details: {{ item.details }} </v-card-subtitle>
					<v-card-text >Description: {{ item.description }}
					</v-card-text>
				</v-col>
			</v-row>
		</v-container>
  	</v-card>
</template>

<script lang="coffee">

export default {
	name: '_slug'


	asyncData: ({ params, $axios, error, store }) ->
		return $axios.get("/api/products/#{params.slug}").then (res) =>
			return { item: res.data }
		.catch (err) =>
			return error({ statusCode: 404, message: 'Post not found' })

};

</script>