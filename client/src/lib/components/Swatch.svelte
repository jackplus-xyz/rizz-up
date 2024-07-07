<script lang="ts">
  export let color: string;
  export let label: string | null | undefined;

  function hexToRgb(hex: string): number[] | null {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? [
          parseInt(result[1], 16),
          parseInt(result[2], 16),
          parseInt(result[3], 16),
        ]
      : null;
  }

  function isDarkColor(color: string): boolean {
    const rgb = hexToRgb(color);
    if (!rgb) return false;
    const [r, g, b] = rgb;
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
    return brightness < 128;
  }

  $: textColor = isDarkColor(color) ? "text-white" : "text-black";
</script>

<div
  class="group flex aspect-square w-full cursor-pointer flex-col items-center justify-center rounded-xl p-2 transition-all duration-200 ease-in-out md:rounded-3xl md:hover:rounded-xl"
  style="background-color: {color};"
>
  <span
    class="duration-50 lg:text-md {textColor} w-full text-center font-mono text-xs font-light opacity-0 transition-opacity duration-500 ease-in-out md:group-hover:opacity-100"
  >
    {label}
  </span>
  <span
    class="duration-50 lg:text-md {textColor} w-full text-center font-mono text-xs font-light opacity-0 transition-opacity duration-500 ease-in-out md:group-hover:opacity-100"
  >
    {color.toUpperCase()}
  </span>
</div>
