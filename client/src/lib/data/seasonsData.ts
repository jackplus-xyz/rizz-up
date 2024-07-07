import { Seasons } from "$lib/types/seasons";

type SeasonsData = {
  [key in Seasons]: SeasonInfo;
};

const seasonsData: SeasonsData = {
  [Seasons.LIGHT_SPRING]: {
    description:
      "Light Springs typically have fair skin with peachy or rosy undertones, which may tan or freckle. Their hair is usually golden blonde or light brown, complemented by blue, green, hazel, or light brown eyes. This season looks best in light, warm, and clear colors that enhance their delicate features. They should avoid dark or overpowering hues that can wash out their natural coloring.",
    colors: [
      "#A69F45",
      "#7DA07A",
      "#1BB17C",
      "#DC3767",
      "#CE4739",
      "#7A80B5",
      "#27B4C8",
      "#836859",
      "#F0EC71",
      "#CCDF86",
      "#74C7B3",
      "#F0A6B7",
      "#F2A595",
      "#D0D2D5",
      "#72C9DB",
      "#D1BE9E",
    ],
  },
  [Seasons.WARM_SPRING]: {
    description:
      "Warm Springs are characterized by warm undertones in their eyes, skin, and hair. Their skin ranges from warm porcelain to light bronze, paired with golden blonde, strawberry blonde, or coppery red hair. Light eyes are common. This season shines in vibrant, warm-toned colors that accentuate their natural glow. They should steer clear of cool-toned pastels and darker shades, while embracing oranges and yellows that highlight their warm intensity.",
    colors: [
      "#ECAB4D",
      "#3B7545",
      "#2E8D80",
      "#D84C63",
      "#B24B42",
      "#745BA3",
      "#2E75B9",
      "#413F40",
      "#E6C568",
      "#90BB53",
      "#49BB74",
      "#EE7F91",
      "#F37E6B",
      "#9C7FB5",
      "#4AA2D6",
      "#6D6660",
    ],
  },
};
