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
	data: ->
		return {
			item: 
				{
					title: "Sauvignon blanc"
					slug: "_sauvignonblanc"
					images: "/images/milestimici/Sauvignon Blanc.png",
					details: "Sauvignon \r\nМин. 10% об \r\nBORDELESA VIP_075L_135KG \r\nAgglomerate cork - sealing capsule",
					description: "Sauvignon 2015– вино марочное сухое белое, золотистого цвета. 
								Вино обладает многогранным и пасленовым букетом, с яркими тонами черной смородины. 
								Характерный вкус свежих цитрусовых и ягод смородины прекрасно раскрывается в бокале. 
								Вино хорошо сочетается с сырами и с блюдами из птицы.",
					item_price: "100.00"
					box_price: "600.00",
					active: true,
					quantity_in_box: 6,
					default_category: null,
					categories: []
				}
		}		
};

</script>