const { execFile } = require('child_process');
const path = require('path');

// 获取可执行文件的路径
const executablePath = path.join(__dirname, 'dist', 'main.exe');

// 调用Python可执行文件
execFile(executablePath, (error, stdout, stderr) => {
    if (error) {
        console.error(`执行出错: ${error}`);
        return;
    }
    console.log(`输出: ${stdout}`);
    if (stderr) {
        console.error(`错误: ${stderr}`);
    }
});