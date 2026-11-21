; Inno Setup script for the ps5-emu Windows desktop installer
#define AppName "ps5-emu"
#define AppVersion "0.9.4"

[Setup]
AppId={{8A1B3C4D-5E6F-7A8B-9C0D-PS5EMU2026}}
AppName={#AppName}
AppVersion={#AppVersion}
DefaultDirName={autopf}\ps5-emu
OutputBaseFilename=ps5emu-{#AppVersion}-setup

[Files]
Source: "..\dist\ps5emu\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{autoprograms}\ps5-emu"; Filename: "{app}\ps5emu.exe"