module.exports.run = async function({ api, args, event }) {
  const { threadID, messageID } = event;

  if (!args[0]) return api.sendMessage("→ Bạn phải nhập 'java' hoặc 'bedrock' để kiểm tra server chính xác", threadID, messageID);
  if (!args[1]) return api.sendMessage("→ Bạn phải nhập ip", threadID, messageID);
  if (!args[2]) return api.sendMessage("→ Bạn phải nhập port", threadID, messageID);

  const mode = args[0].toLowerCase();
  const host = args[1];
  const port = args[2];

  let apiUrl;
  let displayImage = true;
  if (mode === 'java') {
    apiUrl = `https://api.mcstatus.io/v2/status/java/${host}:${port}`;
  } else if (mode === 'bedrock') {
    apiUrl = `https://api.mcstatus.io/v2/status/bedrock/${host}:${port}`;
    displayImage = false;
  } else {
    return api.sendMessage("→ Bạn phải nhập 'java' hoặc 'bedrock' để kiểm tra server chính xác", threadID, messageID);
  }

  api.sendMessage("[𝝡𝗖] Đang Lấy Thông Tin, Vui Lòng Chờ", threadID, messageID);

  try {
    const response = await axios.get(apiUrl);

    let serverInfo;
    if (mode === 'java') {
      serverInfo = response.data;
      const software = serverInfo.software;
      const status = serverInfo.online;
      const online = serverInfo.players.online;
      const max = serverInfo.players.max;
      const motd = serverInfo.motd.clean;
      const version = serverInfo.version.name_raw;
      const msg = serverInfo.msg;

      let messageBody = `》𝐒𝐓𝐀𝐓𝐔𝐒 𝐒𝐄𝐑𝐕𝐄𝐑 𝐌𝐂《\n➜𝙃𝙊𝙎𝙏𝙉𝘼𝙈𝙀 : 「${host}」\n➜𝙋𝙊𝙍𝙏  : 「${port}」\n➜𝙑𝙀𝙍𝙎𝙄𝙊𝙉  : ${version}\n➜𝙎𝙏𝘼𝙏𝙐𝙎: 「${status}」\n➜𝙊𝙉𝙇𝙄𝙉𝙀  : 「${online}/${max}」\n➜𝙈𝙊𝙏𝘿 : ${motd}  \n\n🌺𝐄𝐍𝐃🌺`;

      if (displayImage) {
        const urlimg = mcImageUrl + host + ':' + port + '?dark=true&rounded=false';
        const path = __dirname + '/cache/mcstatus.png';
        const response = await axios.get(urlimg, { responseType: 'arraybuffer' });
        fs.writeFileSync(path, Buffer.from(response.data, 'binary'));

        api.sendMessage(
          {
            body: messageBody,
            attachment: fs.createReadStream(path)
          },
          threadID,
          messageID
        );
      } else {
        api.sendMessage(messageBody, threadID, messageID);
      }
    } else if (mode === 'bedrock') {
      serverInfo = response.data;
      const online = serverInfo.online;
      const on = serverInfo.players.online;
      const version = serverInfo.version.name;
      const max = serverInfo.players.max;
      const motd = serverInfo.motd.clean;

      let messageBody = `》𝐒𝐓𝐀𝐓𝐔𝐒 𝐒𝐄𝐑𝐕𝐄𝐑 𝐌𝐂《\n➜𝙃𝙊𝙎𝙏𝙉𝘼𝙈𝙀 : 「${host}」\n➜𝙋𝙊𝙍𝙏  : 「${port}」\n➜𝙎𝙏𝘼𝙏𝙐𝙎: 「${online}」\n➜𝙑𝙀𝙍𝙎𝙄𝙊𝙉  : ${version}\n➜𝙊𝙉𝙇𝙄𝙉𝙀  : 「${on}/${max}」\n➜𝙈𝙊𝙏𝘿 : ${motd}  \n\n🌺𝐄𝐍𝐃🌺`;

      api.sendMessage(messageBody, threadID, messageID);
    }
  } catch (err) {
    console.log(err);
    return api.sendMessage("→ Không Thể Kết Nối Tới API", threadID);
  }
};
