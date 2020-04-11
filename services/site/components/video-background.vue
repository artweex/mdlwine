<template>
	<section class="VideoBg">
		<video autoplay playsinline loop :muted="muted" ref="video">
			<source
				v-for="source in sources"
				:key="source"
				:src="source"
				:type="getMediaType(source)"
			>
		</video>
		<div class="overlay-content">
			<slot></slot>
		</div>
	</section>
</template>


<script lang="coffee">
	export default {
		props: {
			sources: {
				type: Array,
				required: true
			},
			img: {
				type: String
			},
			muted: {
				type: Boolean,
				default: true
			},
			bottom_offset: {
				type: Number,
				default: 0
			},
			reduce_size: {
				type: Boolean,
				default: false
			}
		},
		data: ->
			return {
				videoRatio: null
			}
		watch: {
			reduce_size: (val) ->
				if val
					@$el.style.height = "#{200}px"
				else
					@$el.style.height = "100%"
				@setVideoSize()
		}
		mounted: ->
			@$nextTick ->
				@setImageUrl()
				@setContainerHeight()
				if @videoCanPlay()
					@$refs.video.oncanplay = () =>
						unless @$refs.video?
							return
						@videoRatio = @$refs.video.videoWidth / @$refs.video.videoHeight
						@setVideoSize()
						@$refs.video.style.visibility = 'visible'
				window.addEventListener('resize', @resize)

		beforeDestroy: ->
			window.removeEventListener('resize', @resize)

		methods: {
			resize: ->
				@setContainerHeight()
				if @videoCanPlay()
					@setVideoSize()

			videoCanPlay: ->
				return @$refs.video.canPlayType?

			setImageUrl: ->
				if @img
					@$el.style.backgroundImage = "url(#{@img})"

			setContainerHeight: ->
				@$el.style.height = "#{window.innerHeight-@bottom_offset}px"

			setVideoSize: ->
				containerRatio = @$el.offsetWidth / @$el.offsetHeight
				if containerRatio > @videoRatio
					width = @$el.offsetWidth
				else
					height = @$el.offsetHeight

				@$refs.video.style.width = if width? then "#{width}px" else 'auto'
				@$refs.video.style.height = if height? then "#{height+1}px" else 'auto'

			getMediaType: (src) ->
				return 'video/' + src.split('.').pop()

		}
	}
</script>


<style scoped lang="scss">
.VideoBg
{
	position: relative;
	background-size: cover;
	background-position: center;
	overflow: hidden;
	transition: all 0.3s linear;
	video
	{
		position: absolute;
		top: 50%;
		left: 50%;
		visibility: hidden;
		transform: translate(-50%, -50%);
	}
	.overlay-content
	{
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	}
}
</style>