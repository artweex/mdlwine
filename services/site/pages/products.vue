<template>
  <section class="products" >
	  <product-card v-for="(product, key) in products" :key="key" :item="product"/>
  </section>
</template>

<script lang="coffee">
import ProductCard from "~/components/product-card"
export default {
	name: 'products'
	components:
		"product-card": ProductCard
		
	asyncData: ({ params, $axios, error, store }) ->
		return $axios.get("/api/products").then (res) =>
			return { products: res.data }
		.catch (err) =>
			return error({ statusCode: 404, message: 'Post not found' })
		
   ###
	data: ->

		return {
			
			products: [
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
				{
					title: "Negre de Milestii Mici",
					slug: "_negremilestiimici",
					images: "/images/milestimici/negre_milestemich_2011.png",
					details: "Cabernet-Sauvignon, Rară Neagră, Saperavi\r\n 
							  Мин. 10,5% об. \r\n
							  BORDELESA VIP_075L_135KG \r\n
							  Agglomerate cork - sealing capsule",
					description: "Negru de Milestii Mici 2011 – вино марочное сухое красное, темно-рубинового, насыщенного цвета, произведенное из 					  винограда сортов Cabernet-Sauvignon, Rara Neagra и Saperavi.
					             Богатый букет черной смородины, шафрана и чернослива прекрасно дополняет бархатистый вкус. Приятная терпкость и восхитительное, продолжительное после вкусье позволяет этому вину быть хорошим дополнением к тушеному и жареному мясу говядины.",
					item_price: "300.00",
					box_price: "1800.00",
					active: true,
					quantity_in_box: 6,
					default_category: null,
					categories: []
				}
				{
					title: "Merlot 2015",
					slug: "_merlout2015",
					images: "/images/milestimici/merlot_2015.png",
					details: "Min 12,5 % vol. - 160 g/dm3 \r\nBordelesa Storica 0,75 l/ 1,35 кg \r\nNatural cork, red wax",
					description: "Срок выдержки в дубовой таре от шести месяцев до несколько лет. Удивительные вина, которые после созревания в дубовой таре обретают массу вкусовых особенностей. Их розлив осуществляется непосредственно перед реализацией.",
					item_price: "200.00",
					box_price: "1200.00",
					active: true,
					quantity_in_box: 6,
					default_category: null,
					categories: []
				}
				{
					title: "Merlot 2014",
					slug: "_merlout2014",
					images: "/images/milestimici/merlot_2014.png",
					details: "Min 12,5 % vol. - 160 g/dm3 \r\n
							 Bordelesa Storica 0,75 l/ 1,35 кg \r\n
							 Natural cork, red wax",
					description: "Merlot 2015 – вино сухое красное, темно-красного цвета, с рубиновым оттенком. 
									Выделяется насыщенным, хорошо слаженным букетом с тонами паслена в дополнении нюансов лесных ягод и спелых красных фруктов. 
									Вино обладает хорошо структурированным, легким  танинным вкусом. 
									Этот напиток хороший партнер к приготовленному на гриле красному мясу, паштетам, 
									жаркому, спагетти и твердым сырам.",
					item_price: "100.00",
					box_price: "600.00",
					active: true,
					quantity_in_box: 6,
					default_category: null,
					categories: []	
				}
				
			]
			
		}
	###	
}

</script>

<style lang="scss" scoped>
section
{
	&.products
	{
		padding: 8px;
		display: grid;
		grid-gap: 8px;
		grid-template-columns: repeat(auto-fill, minmax(45%, 1fr));
	}
}
</style>