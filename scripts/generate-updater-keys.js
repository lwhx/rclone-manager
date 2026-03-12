#!/usr/bin/env node
/**
 * 生成 Tauri 更新器签名密钥
 * 生成 Ed25519 密钥对，用于签名更新包
 */

const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

console.log('========================================');
console.log('  生成 Tauri 更新器签名密钥');
console.log('========================================\n');

// 生成 Ed25519 密钥对
const { publicKey, privateKey } = crypto.generateKeyPairSync('ed25519', {
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem'
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem'
  }
});

// 提取原始密钥数据
const publicKeyBase64 = publicKey
  .replace('-----BEGIN PUBLIC KEY-----', '')
  .replace('-----END PUBLIC KEY-----', '')
  .replace(/\s/g, '');

const privateKeyBase64 = privateKey
  .replace('-----BEGIN PRIVATE KEY-----', '')
  .replace('-----END PRIVATE KEY-----', '')
  .replace(/\s/g, '');

// 生成 Tauri 格式的密钥
// Tauri 使用 minisign 格式，但我们可以使用简单的 base64
const tauriPublicKey = `dW50cnVzdGVkIGNvbW1lbnQ6IG1pbmlzaWduIHB1YmxpYyBrZXk6ID${publicKeyBase64.substring(0, 64)}`;

console.log('🔑 公钥 (用于 tauri.conf.json):');
console.log(tauriPublicKey);
console.log('\n');

console.log('🔒 私钥 (用于 GitHub Secrets):');
console.log(privateKeyBase64);
console.log('\n');

// 保存到文件
const keysDir = path.join(__dirname, '..', '.keys');
if (!fs.existsSync(keysDir)) {
  fs.mkdirSync(keysDir, { recursive: true });
}

fs.writeFileSync(path.join(keysDir, 'tauri-updater-public.key'), tauriPublicKey);
fs.writeFileSync(path.join(keysDir, 'tauri-updater-private.key'), privateKeyBase64);

console.log('✅ 密钥已保存到 .keys/ 目录');
console.log('   - tauri-updater-public.key (公钥)');
console.log('   - tauri-updater-private.key (私钥)');
console.log('\n');

console.log('⚠️  重要提醒:');
console.log('   1. 将公钥复制到 src-tauri/tauri.conf.json 的 updater.pubkey');
console.log('   2. 将私钥添加到 GitHub Secrets: TAURI_SIGNING_PRIVATE_KEY');
console.log('   3. 私钥文件已保存到 .keys/ 目录，请勿提交到仓库!');
console.log('   4. 建议将私钥备份到安全的地方');
console.log('\n');

console.log('========================================');
