# AR Cam

A marker based augmented reality camera app for the web. Powered by [AR.js](https://github.com/AR-js-org/AR.js). Fast, light-weight and works on any mobile/desktop browser with [WebGL](https://get.webgl.org/) and [WebRTC](https://webrtc.org/).

![doggy](https://cdn.glitch.me/f6a3b56b-85a4-42bf-a1b9-dc91a0db78de/ar-vid.gif?v=1713077885726)

- Monitor any traffic junction with ease by scanning the marker, ANYPLACE & ANYTIME!
- Snap and save pictures to work with convenience.
- Tested in Chrome and Safari.

## How it works

- The link to video of traffic bottlenecks detected in a particular traffic junction is linked using `a-entity` tag in `index.html`. [Learn more](https://ar-js-org.github.io/AR.js-Docs/marker-based/#a-frame).
- By default the marker is preset to the [hiro marker](https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png). To create a custom marker for each location,
  - Use [this tool](https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html) to create your custom marker.
  - Export the `.patt` file and place it in `/assets/custom-markers/`.
  - Link it using `a-marker` tag in `index.html`. [Learn more](https://ar-js-org.github.io/AR.js-Docs/marker-based/#a-frame).
  - You may follow [this article](https://ar-js-org.github.io/AR.js-Docs/marker-based/#how-to-choose-good-images-for-pattern-markers) to create an effective custom marker.
  
## How to use

- Fire up the app and point it to the marker. Default hiro marker can be found [here](https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png).
- Translate, rotate or zoom the model as desired and snap a pic!

## Dependencies

| Dependency | Purpose                         |
| ---------- | ------------------------------- |
| AR.js      | Implements AR on the web.       |
| A-Frame    | Renders augmented content.      |
| three.js   | Renders augmented content.      |
| ZingTouch  | Gesture controls for the model. |

## Always deploy under https

All AR.js web apps in general, have to be run on a server. You can use local server or deploy the static web app on the web. Might run into permission errors in http. So don't forget to always run your examples on secure connections servers or localhost. Github Pages is a great way to have free and live websites under https.

## Demo

Checkout a live deployment [here](https://divinsmathew.github.io/ar-cam/). Use the [hiro marker](https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png) to see the video as Augmented Reality!

## Scope

Scope of improvement includes:

- Ability to record video.
- Advanced gesture controls.
- Improved antialiasing of snaps.
- Suppport for portrait mode.

