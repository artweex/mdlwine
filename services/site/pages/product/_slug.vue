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
					<v-card-subtitle class="pa-1 pt-5"
					>
						<v-icon>mdi-fruit-grapes-outline</v-icon>
						{{ item.details.split(/\r\n/)[0] }}
					</v-card-subtitle>
					<v-card-subtitle class="pa-1"
					>
						<v-icon>mdi-glass-wine</v-icon>
						{{ item.details.split(/\r\n/)[1] }}
					</v-card-subtitle>
					<v-card-subtitle class="pa-1"
					>
						<v-icon>mdi-flask-outline</v-icon>
						{{ item.details.split(/\r\n/)[2] }}
					</v-card-subtitle>
					<v-card-subtitle class="pa-1"
					>
						<v-icon>mdi-toggle-switch</v-icon>
						{{ item.details.split(/\r\n/)[3] }}
					</v-card-subtitle>
					<v-card-text >Description: {{ item.description }}
					</v-card-text>
				</v-col>
			</v-row>
		</v-container>
  	</v-card>
</template>

<script lang="coffee">

export default {
	name: 'slug'
	

	asyncData: ({ params, $axios, error, store }) ->
		return $axios.get("/api/products/#{params.slug}").then (res) =>
			return { item: res.data }
		.catch (err) =>
			return error({ statusCode: 404, message: 'Post not found' })
	
	
		
	
		
};

</script>