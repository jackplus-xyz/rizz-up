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

  function isExtremeBrightness(color: string): boolean {
    const rgb = hexToRgb(color);
    if (!rgb) return false;
    const [r, g, b] = rgb;
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
    return brightness < 30 || brightness > 225;
  }

  function getTextColor(color: string): string {
    const rgb = hexToRgb(color);
    if (!rgb) return "text-black";
    const [r, g, b] = rgb;
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
    return brightness < 128 ? "text-white" : "text-black";
  }

  $: textColor = getTextColor(color);
  $: needsBorder = isExtremeBrightness(color);
</script>

<div
  class="{needsBorder
    ? 'border-2 border-muted'
    : ''} group flex aspect-square w-full cursor-pointer flex-col items-center justify-center rounded-xl p-2 transition-all duration-200 ease-in-out md:rounded-2xl md:hover:rounded-lg lg:rounded-3xl lg:hover:rounded-xl"
  style="background-color: {color};"
>
  <span
    class="duration-50 lg:text-md {textColor} w-full text-center font-mono text-xs font-light opacity-0 transition-opacity duration-500 ease-in-out max-sm:hidden md:group-hover:opacity-100"
  >
    {label}
  </span>
  <span
    class="duration-50 lg:text-md {textColor} w-full text-center font-mono text-xs font-light opacity-0 transition-opacity duration-500 ease-in-out max-sm:hidden md:group-hover:opacity-100"
  >
    {color.toUpperCase()}
  </span>
</div>
