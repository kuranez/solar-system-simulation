const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const versionsDir = './versions';
const changelogFile = './CHANGELOG.md';

// Get sorted versions
const versions = fs.readdirSync(versionsDir)
  .filter((d) => fs.lstatSync(path.join(versionsDir, d)).isDirectory())
  .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));

let changelog = '# Changelog\n\n';

for (let i = 1; i < versions.length; i++) {
  const prev = versions[i - 1];
  const curr = versions[i];

  changelog += `## ${curr}\n`;

  // Use diff to find changes between folders
  const diff = spawnSync('diff', ['-ru', path.join(versionsDir, prev), path.join(versionsDir, curr)], {
    encoding: 'utf8'
  });

  if (diff.stdout) {
    // Simple summary: list added/removed files. For full details, parse diff.stdout.
    const lines = diff.stdout.split('\n');
    lines.forEach(line => {
      if (line.startsWith('Only in')) {
        changelog += `- ${line}\n`;
      } else if (line.startsWith('diff')) {
        changelog += `- Changed file: ${line.split(' ').pop()}\n`;
      }
    });
  } else {
    changelog += '- No changes\n';
  }
  changelog += '\n';
}

fs.writeFileSync(changelogFile, changelog);
console.log('Changelog generated in CHANGELOG.md');