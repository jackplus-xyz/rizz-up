export enum Seasons {
  LIGHT_SPRING = "Light Spring",
  WARM_SPRING = "Warm Spring",
  BRIGHT_SPRING = "Bright Spring",
  LIGHT_SUMMER = "Light Summer",
  COOL_SUMMER = "Cool Summer",
  SOFT_SUMMER = "Soft Summer",
  SOFT_AUTUMN = "Soft Autumn",
  WARM_AUTUMN = "Warm Autumn",
  DEEP_AUTUMN = "Deep Autumn",
  DEEP_WINTER = "Deep Winter",
  COOL_WINTER = "Cool Winter",
  BRIGHT_WINTER = "Bright Winter",
}

export interface SeasonInfo {
  description: string;
  colors: string[];
  textColor: string;
}
