import { Config } from "@remotion/cli/config";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
// 2 tabs: the default (all cores) got killed ~84% into 10-min lessons.
Config.setConcurrency(2);
Config.setDelayRenderTimeoutInMilliseconds(120000);
// Own port: other dev servers on :3000 (e.g. a Next.js app) answered Remotion's
// asset requests with 404s and killed renders mid-way.
Config.setPort(3927);  // English project uses 3917: Indian-language renders never clash with it
