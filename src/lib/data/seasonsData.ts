import { Seasons } from "$lib/types/seasons";
import type { SeasonInfo } from "$lib/types/seasons";

export const seasonsData: Record<Seasons, SeasonInfo> = {
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
    textColor: "text-[#4A7C59]",
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
    textColor: "text-[#8B6E4E]",
  },
  [Seasons.BRIGHT_SPRING]: {
    description:
      "Bright Springs encompass a wide range of features, including various hair colors from blonde to dark brown, sometimes with red or copper highlights. Their skin tones span from pale to golden brown and black, while their eyes often display a mix of colors such as blue, green, brown, or topaz. This season thrives in saturated, warm hues with a touch of coolness. They should avoid muted or dusty pastels and nudes, as these can wash them out. High-contrast and bright colors are their forte, allowing them to stand out brilliantly.",
    colors: [
      "#254F92",
      "#2F4579",
      "#235076",
      "#423E65",
      "#644895",
      "#8C62A4",
      "#602884",
      "#018A42",
      "#39B3BE",
      "#1D8682",
      "#53BED1",
      "#00707E",
      "#5C9ACB",
      "#277DBB",
      "#E6475D",
      "#E6648E",
      "#E04673",
      "#BE3161",
      "#91B748",
      "#5B9C34",
      "#31783C",
      "#FDEDA7",
      "#F4CA6E",
      "#E89F46",
      "#E9704D",
      "#EC887E",
      "#E75C48",
      "#D8283D",
    ],
    textColor: "text-[#E37D5E]",
  },
  [Seasons.LIGHT_SUMMER]: {
    description:
      "Light Summers typically have neutral skin that burns easily and may have a rosy tint. Their hair is often icy blonde or very light brown, paired with light-colored eyes such as blue, green, or gray. This season looks best in light, dusty, or powdery colors that complement their delicate features without overpowering them. They should generally avoid dark colors or high-saturation warm tones, which can clash with their subtle coloring.",
    colors: [
      "#F6D087",
      "#2CA17C",
      "#2A8598",
      "#E1465F",
      "#AE5374",
      "#5B5488",
      "#315184",
      "#596774",
      "#F2DAB4",
      "#84CDB2",
      "#75CCDD",
      "#F07182",
      "#F19BB8",
      "#9885BD",
      "#90ADD7",
      "#CCD0D5",
    ],
    textColor: "text-[#7C90A0]",
  },
  [Seasons.COOL_SUMMER]: {
    description:
      "Cool Summers have cool or blue undertones in their skin, hair, and eyes. Their skin tones are often cool or neutral, with grey, blue, or slate eyes. Ashy hair tones ranging from medium to dark brown (not black) are common. This season excels in cool hues of medium to sometimes dark shades, with a muted quality and blue-pink undertones. They should avoid warm tones, especially yellow-based hues or earthy warm shades, as these can clash with their cool coloring.",
    colors: [
      "#A2C1EB",
      "#70AED5",
      "#4675AD",
      "#305587",
      "#9393C3",
      "#665D94",
      "#4D4477",
      "#79C1AA",
      "#148E8D",
      "#339B88",
      "#007958",
      "#71C2E1",
      "#0191A0",
      "#077288",
      "#EA6F8D",
      "#E881A0",
      "#C15372",
      "#92495B",
      "#F6C0D6",
      "#C47598",
      "#963C64",
      "#D6CACA",
      "#BEA59F",
      "#5F4D4F",
      "#BCBFC2",
      "#50575E",
      "#7B989A",
      "#43808F",
    ],
    textColor: "text-[#5E7C8B]",
  },
  [Seasons.SOFT_SUMMER]: {
    description:
      "Soft Summers have neutral or blue undertones with a pink tint, or brown skin tones with a neutral undertone. Their hair is typically light to medium brown with ash blonde highlights or tints. This season has low contrast between eyes, hair, and skin, and looks best in soft, muted hues that are more subtle and cool-leaning. They should generally avoid clear, neon, or rich colors that can overwhelm their delicate complexion. Their palette ranges from light stone to charcoal, with a soft, ethereal quality.",
    colors: [
      "#A0C1EA",
      "#70AED5",
      "#4675AD",
      "#305587",
      "#9492C3",
      "#665D93",
      "#4F4679",
      "#79C1AA",
      "#449882",
      "#2F6A5F",
      "#007958",
      "#71C2E1",
      "#4CB5C6",
      "#077288",
      "#EB859E",
      "#E96885",
      "#C15372",
      "#F4C1D6",
      "#C47598",
      "#92495b",
      "#963C64",
      "#D6CACA",
      "#AA8B8D",
      "#5F4D4F",
      "#929AA5",
      "#6F7B95",
      "#BDC9CB",
      "#7097A2",
    ],
    textColor: "text-[#8B8BAA]",
  },
  [Seasons.SOFT_AUTUMN]: {
    description:
      "Soft Autumns have little contrast between their hair and skin. Their skin tone often has neutral undertones, but can also have more prominent warm undertones. This season looks best in muted colors with warm undertones that complement their skin's hue. They excel in blended colors rather than primary hues. Soft Autumns should generally avoid stark colors like black or bright, highly pigmented shades such as fuchsia, as these can make them appear sallow.",
    colors: [
      "#78AACB",
      "#33618A",
      "#2D4F68",
      "#6D709B",
      "#707EAF",
      "#4D5B82",
      "#414141",
      "#93926A",
      "#A6D1B5",
      "#86BC9C",
      "#5F8D79",
      "#478F85",
      "#247674",
      "#366045",
      "#EFA4A2",
      "#EC827E",
      "#F4C4BA",
      "#E88484",
      "#A24B4A",
      "#6E6A57",
      "#929D7A",
      "#E0B88D",
      "#CCA480",
      "#A47C65",
      "#9E6C61",
      "#694D4F",
      "#F1D48E",
      "#CBB178",
    ],
    textColor: "text-[#8B7E66]",
  },
  [Seasons.WARM_AUTUMN]: {
    description:
      "Warm Autumns have warm undertones in their skin, which can range from ivory to medium brown. Their hair typically ranges from medium to dark brown or red (including auburn) with golden undertones. Eyes are often light brown, green, or (green) hazel. This season shines in rich and muted warm tones, especially earthy colors like brown and rust. They should generally avoid pastels or bright pastels that can wash them out. Their palette is characterized by pumpkin oranges, butterscotch, and terracotta, with all hues warmed up and toned down.",
    colors: [
      "#867C41",
      "#57843D",
      "#2E543D",
      "#20828D",
      "#1F5E6D",
      "#856C9C",
      "#653D60",
      "#E09758",
      "#C56248",
      "#E06450",
      "#B64C34",
      "#E5727D",
      "#8F4345",
      "#ABB175",
      "#F4DBA5",
      "#C1974D",
      "#846D41",
      "#B47C65",
      "#996457",
      "#FDD077",
      "#DFB16B",
      "#C7C089",
      "#E9DCC2",
      "#F4DBA5",
      "#B6A27E",
      "#B9A07A",
      "#928167",
      "#6F5D4F",
    ],
    textColor: "text-[#A0522D]",
  },
  [Seasons.DEEP_AUTUMN]: {
    description:
      "Deep Autumns have warm tones in their hair, eyes, and skin. Their hair is typically medium to dark brown with golden undertones, while their eyes range from dark blue and green to dark brown or brown/black. This season excels in bold, warm colors that are rich in pigment. They should generally avoid dusty colors or soft pastels, as these can make them look washed out. Their palette focuses on depth, transitioning from pumpkin oranges to brick reds and warm redwood colors, with slightly more pigmentation than True Autumn.",
    colors: [
      "#D4A0BA",
      "#C0789A",
      "#A64E7A",
      "#804160",
      "#A09255",
      "#7F723C",
      "#5E5538",
      "#60BAB6",
      "#399896",
      "#105D4B",
      "#2E4740",
      "#2F98B9",
      "#006B81",
      "#034C5E",
      "#E88468",
      "#C16E53",
      "#82473F",
      "#ED8576",
      "#672C37",
      "#903427",
      "#8B2026",
      "#6D5C58",
      "#503E48",
      "#636A3A",
      "#40463A",
      "#D7B569",
      "#B99555",
      "#BE7E57",
    ],
    textColor: "text-[#8B4726]",
  },
  [Seasons.DEEP_WINTER]: {
    description:
      "Deep Winters have a rich and high-contrast appearance. Their skin tones are not purely cool and could be considered more neutral, including olive complexions. They typically have dark eyes and dark hair. This season looks best in high saturation colors, rich primary colors, and pure pigments. They should avoid earthy tones, warm nudes, or warm-toned browns, oranges, and yellows, as these can clash with their coloring.",
    colors: [
      "#913D4B",
      "#B690B7",
      "#A96BAA",
      "#773E72",
      "#523955",
      "#5B3443",
      "#3E1C4D",
      "#07776C",
      "#0682B2",
      "#2473A8",
      "#7DB1E4",
      "#6799CC",
      "#2C6FB1",
      "#35426E",
      "#CD3851",
      "#E15564",
      "#893F41",
      "#25A87A",
      "#007255",
      "#205749",
      "#2B381D",
      "#C8DDD4",
      "#BBD2E5",
      "#F7E069",
      "#8DAB41",
      "#637E3D",
      "#EA5E73",
      "#CD4D7D",
    ],
    textColor: "text-[#4A4E69]",
  },
  [Seasons.COOL_WINTER]: {
    description:
      "Cool Winters often have high contrast between their hair, skin tone, and eyes. They excel in icy colors and cool hues, with darker values working well as long as they have a cool undertone. This season should avoid warm-toned colors for the most flattering pairings. Instead of pastels, they should opt for icier colors (high saturation + white). Note that not every Cool Winter will have the classic 'Snow White' appearance, and draping is the most accurate way to determine this season.",
    colors: [
      "#B77EB5",
      "#92457F",
      "#7B4889",
      "#5B4D98",
      "#524378",
      "#3C60A8",
      "#434476",
      "#F4CFE4",
      "#EDB9D1",
      "#EA6EA6",
      "#C73C73",
      "#D0639F",
      "#D75C8F",
      "#B73F7B",
      "#2165B0",
      "#39A8E1",
      "#0D7388",
      "#27A6BA",
      "#066555",
      "#018854",
      "#30AA63",
      "#C12A2F",
      "#D02E4F",
      "#FEE607",
      "#FEEA7B",
      "#C8E4EE",
      "#C5DDC1",
      "#BBB",
    ],
    textColor: "text-[#4A6670]",
  },
  [Seasons.BRIGHT_WINTER]: {
    description:
      "Bright Winters can have a variety of characteristics, including the possibility of bright red hair and sparkling eyes. Their 'brightness' is determined by how fabric drapes react to their coloring, rather than an obvious high contrast appearance. This season looks best in clear, vivid colors that allow their natural coloring to shine. They should avoid muted or toned-down shades that can dull their vibrant features. Note that even 'bright' seasons look relatively normal in everyday life, and accurate typing requires professional color analysis.",
    colors: [
      "#9E3283",
      "#823281",
      "#51428D",
      "#48539F",
      "#353D8E",
      "#7465A9",
      "#423B8D",
      "#06984B",
      "#046E3A",
      "#029598",
      "#8CB9E2",
      "#0288CB",
      "#0257A5",
      "#23427A",
      "#EC7F88",
      "#E4414E",
      "#E12540",
      "#EC8BB5",
      "#E32F68",
      "#D6194D",
      "#CE2F85",
      "#F3D0E2",
      "#C0DFCE",
      "#DACAE3",
      "#FBEB80",
      "#FFE56A",
      "#A7C545",
      "#83AB58",
    ],
    textColor: "text-[#5E548E]",
  },
};