const embed = window['sisense.embed'];
const SisenseFrame = embed.SisenseFrame;
const enums = embed.enums;

const sisenseFrame = new SisenseFrame({
  // Sisense application URL, including protocol and port if required
  url: 'https://iprotech.sisensepoc.com',
  // OID of dashboard to load initially
  dashboard: '5fa9b6ac62aa35002d4de013',
  // Which panels to show in the iFrame
  settings: {
    showLeftPane: true,
    showToolbar: true,
    showRightPane: false,
  },
  // You can define existing <iframe/> DOM element here or
  // pass some <div/> as a parameter to render function below
  // and <iframe/> will be rendered inside that <div/> dynamically
  element: document.getElementById('sisense-frame')
});

sisenseFrame.render().then(() => {
  console.log("Sisense iFrame ready!");
});
