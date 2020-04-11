<template>
	<div class="base">
		<div class="wrapper" ref="wrapper">
			<div ref="scroller" :class="{ 'horizontal': horizontal }">
				<slot></slot>
			</div>
		</div>
	</div>
</template>
<script lang="coffee">
import IScroll from './vender/iscroll.js'
# import sticky from './vender/iscroll.stickyheaders.js'
export default {
	name: 'i-scroll'
	data: ->
		return {
			myScroll: null
			scroller: null
			size: { width: 0, height: 0 }
			interval: null
		}

	props:
		color: null
		horizontal:
			type: Boolean
			default: false

		vertical:
			type: Boolean
			default: true

		autoScrollDown:
			type: Boolean
			default: false

		sticky:
			type: String
			default: ''

	mounted: ->
		@$nextTick ->
			@init()
			@reset()
			@interval = setInterval =>
				if @scroller is null
					@scroller = @$refs.scroller
				else
					@size = { width: @scroller.clientWidth, height: @scroller.clientHeight }
			, 300

	updated: ->
		@$nextTick ->
			@reset()

	beforeDestroy: ->
		clearInterval(@interval)
		@myScroll.destroy()
		@myScroll = null
		@scroller = null

	watch:
		size:
			handler: (val, old_val) ->
				if val.height != old_val.height
					@reset()
			deep: true


	methods:

		init: ->
			wrapper = @$refs.wrapper
			if wrapper?
				@myScroll = new IScroll(wrapper, {
					scrollbars: true,
					mouseWheel: true,
					scrollX: @horizontal,
					scrollY: @vertical,
					freeScroll: @horizontal,
					useTransition: true,
					interactiveScrollbars: true,
					shrinkScrollbars: 'scale',
					scrollbars: 'custom',
					fadeScrollbars: false,
					preventDefault: false,
					# eventPassthrough: true,
				})
				# unless @sticky == ''
				# 	@myScroll.enableStickyHeaders(@sticky)

		reset: ->
			if @myScroll?
				setTimeout ( =>
					unless @myScroll is null
						@myScroll.refresh()
				), 300

				if @autoScrollDown
					@myScroll.scrollTo(0, -@size.height)
			else
				@init()
}
</script>
<style lang="scss">
.base
{
	overflow: hidden;
	display: block;
	position: relative;
	height: 100%;
	// top: 0;
	// bottom: 0;
	// left: 0;
	// right: 0;
}
.wrapper
{
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	box-sizing: border-box;
	position: relative;
	// z-index: 1;
	// top: 45px;
	// bottom: 48px;
	// left: 0;
	width: 100%;
	height: 100%;
	// max-height: calc(100vh - 476px);
	// background: #ccc;
	padding-right: 14px;
	overflow: hidden;
	display: block;
	& > div:not(.iScrollHorizontalScrollbar)
	{
		// display: inline-block;
		overflow: hidden;
		-webkit-box-sizing: border-box;
		-moz-box-sizing: border-box;
		box-sizing: border-box;
		height: auto;

		// width: auto;
		// position: sticky;
		// top:0;
		// position: relative;
	}
}
#scroller
{
	// min-width: 100%;
	// float: left;
}
.horizontal
{
	display: inline-block;
	min-width: 100%;
}
.iScrollVerticalScrollbar
{
	background-color: rgba( 0, 0, 0, 0.1 );
	border-radius: 3px;
	position: absolute;
	width: 7px;
	bottom: 2px;
	top: 2px;
	right: 1px;
	overflow: hidden;
	.iScrollIndicator
	{
		box-sizing: border-box;
		position: absolute;
		background: rgba(0, 0, 0, 0.5) none repeat scroll 0% 0%;
		// border: 1px solid rgba(255, 255, 255, 0.9);
		border-radius: 3px;
		width: 100%;
		transition-duration: 0ms;
		display: block;
		height: 437px;
		transform: translate(0px, 0px) translateZ(0px);
		transition-timing-function: cubic-bezier(0.1, 0.57, 0.1, 1);
	}
}

.iScrollHorizontalScrollbar
{
	background-color: rgba(88, 89, 91, 0.1);
	border-radius: 3px;
	position: absolute;
	height: 7px;
	bottom: 2px;
	left: 2px;
	right: 14px;
	overflow: hidden;
	.iScrollIndicator
	{
		box-sizing: border-box;
		position: absolute;
		background: rgba(88, 89, 91, 0.8) none repeat scroll 0% 0%;
		// border: 1px solid rgba(255, 255, 255, 0.9);
		border-radius: 3px;
		width: 437px;
		transition-duration: 0ms;
		display: block;
		height: 100%;
		transform: translate(0px, 0px) translateZ(0px);
		transition-timing-function: cubic-bezier(0.1, 0.57, 0.1, 1);
	}
}
</style>
