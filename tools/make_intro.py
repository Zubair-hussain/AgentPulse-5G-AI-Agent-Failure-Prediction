"""Render original six-scene 30s WebM using Pillow, FFmpeg and eSpeak."""
from pathlib import Path
import json, subprocess, tempfile, math
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'assets'; OUT.mkdir(exist_ok=True)
scenes=[('01 / THE PROBLEM','AI agents fail.','Can we predict the failure before it happens?','AI agents fail. Can we predict failure before it happens?'),('02 / THE DATA','20,000 demo runs','16 numerical signals • 20 synthetic shards','Twenty thousand synthetic agent runs, with sixteen telemetry signals.'),('03 / THE METHOD','Telemetry → risk','Train / validation / test • separate cohorts','Train on telemetry, validate thresholds, and test on separate cohorts.'),('04 / THE BENCHMARK','0.765 ROC-AUC','Logistic baseline • held-out synthetic test','The logistic baseline achieves point seven six five ROC A U C on synthetic test data.'),('05 / THE DEPLOYMENT','No prompt. No API key.','Local JSON scoring • Python • FastAPI','Score failure risk locally, with no prompt and no API key.'),('06 / OPEN RESEARCH','AgentPulse-5G','MIT • Zubair Hussain • zubairhussain.xyz','Agent Pulse. Open research by Zubair Hussain. Build, test, and contribute.')]
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def draw_scene(i):
    im=Image.new('RGB',(1280,720),'#0a1523'); d=ImageDraw.Draw(im)
    for x in range(0,1280,48): d.line((x,0,x,720),fill='#142638')
    for y in range(0,720,48): d.line((0,y,1280,y),fill='#142638')
    d.rounded_rectangle((48,45,1232,675),radius=26,fill='#0d1c2c',outline='#23435a',width=2)
    d.text((86,86),'AGENTPULSE / RESEARCH LAB',font=ImageFont.truetype(bold,24),fill='#63e4cf')
    d.text((86,182),scenes[i][0],font=ImageFont.truetype(bold,23),fill='#89a5ba')
    d.text((86,235),scenes[i][1],font=ImageFont.truetype(bold,57),fill='#f0f8ff')
    d.text((86,320),scenes[i][2],font=ImageFont.truetype(font,29),fill='#a8c4d9')
    pts=[(86+j*18,490+int(32*math.sin(j*.38+i)+13*math.cos(j*.95))) for j in range(61)]
    d.line(pts,fill='#46dac6',width=4)
    for j in range(6): d.rounded_rectangle((86+j*184,593,86+j*184+164,600),radius=3,fill='#52e4ce' if j<=i else '#284559')
    d.text((86,624),'SYNTHETIC DATA  /  NOT PRODUCTION VALIDATED',font=ImageFont.truetype(font,19),fill='#7894a9')
    return im

def run():
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp); segs=[]
        for i,scene in enumerate(scenes):
            img=p/f'{i}.png'; draw_scene(i).save(img)
            wav=p/f'{i}.wav'; subprocess.run(['espeak','-s','175','-w',str(wav),scene[3]],check=True)
            dst=p/f'{i}.webm'; subprocess.run(['ffmpeg','-loglevel','error','-y','-loop','1','-framerate','24','-i',str(img),'-i',str(wav),'-af','apad','-t','5','-c:v','libvpx-vp9','-b:v','0','-crf','34','-pix_fmt','yuv420p','-c:a','libopus','-b:a','48k',str(dst)],check=True); segs.append(dst)
        listing=p/'concat.txt'; listing.write_text(''.join(f"file '{f}'\n" for f in segs)); subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',str(listing),'-c','copy',str(OUT/'intro.webm')],check=True)
    draw_scene(0).save(OUT/'cover.png')
    (OUT/'intro.vtt').write_text('WEBVTT\n\n'+''.join(f'00:{i*5:02d}.000 --> 00:{(i+1)*5:02d}.000\n{s[3]}\n\n' for i,s in enumerate(scenes)))
if __name__=='__main__':run()
