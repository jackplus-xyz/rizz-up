<script lang="ts">
  import { spring } from "svelte/motion";
  import ArrowLink from "$lib/components/ArrowLink.svelte";
  import GuidanceLeft2ShortArrow from "~icons/guidance/left-2-short-arrow";

  let arrowTransform = spring(0, {
    stiffness: 0.1,
    damping: 0.2,
  });

  function scrollToUpload(elementId: string) {
    const elementToScrollTo = document.getElementById(elementId);

    if (!elementToScrollTo) {
      console.warn(`Element with ID '${elementId}' not found.`);
      return;
    }

    elementToScrollTo.scrollIntoView({ behavior: "smooth" });

    const animateArrow = (transformValue: number, delay: number) => {
      setTimeout(() => {
        arrowTransform.set(transformValue);
      }, delay);
    };

    animateArrow(10, 200);
    animateArrow(0, 400);
  }
</script>

<div class="flex flex-col items-center justify-center space-y-8 py-8 md:py-32">
  <h1
    class="animate-gradient flex flex-col bg-gradient-to-r from-amber-900 via-orange-200 to-orange-600 bg-clip-text text-center font-serif text-xl font-bold text-transparent md:text-5xl"
  >
    Unlock Your Personal Color Palette with <i class="mt-4 text-5xl md:text-8xl"
      >Rizz Up</i
    >
  </h1>
  <p class="text-md mx-auto px-8 text-center font-serif md:px-4 md:text-2xl">
    Discover the perfect colors that complement your skin tone and style. And,
    finally find harmony in your wardrobe.
  </p>
  <div
    class="flex flex-col space-y-8 pt-4 text-lg font-light md:flex-row md:space-x-16 md:space-y-0 md:pt-16 md:text-2xl"
  >
    <ArrowLink link="/about" text="Learn More" />
    <button
      on:click={() => scrollToUpload("upload-image")}
      class="group hidden items-center text-lg font-light md:flex md:text-2xl"
    >
      Get Started
      <span class="ml-2 transition-all group-hover:translate-x-2 md:ml-4">
        <GuidanceLeft2ShortArrow />
      </span>
    </button>
  </div>
</div>

<style>
  .animate-gradient {
    background-size: 300%;
    -webkit-animation: animatedgradient 6s ease infinite alternate;
    -moz-animation: animatedgradient 6s ease infinite alternate;
    animation: animatedgradient 6s ease infinite alternate;
  }

  @keyframes animatedgradient {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }
</style>
