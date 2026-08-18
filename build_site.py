#!/usr/bin/env python3
"""Build the PB Trading swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/PB_TRADING_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {'PBTrading_VSL.mp4': 'The main VSL, served by ConverteAI.'}

CONFIG = {
 "SITE": "PB Trading — First Payout",
 "CREATOR": "PB Trading",
 "ADS_KEY": "pbtrading",
 "FUNNEL_IDS": ["F080"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/PB_TRADING_Swipe",
 "BLURB": "Prop-firm trading education. The headline counts in <b>payouts and consecutive days</b>, "
          "not dollars &mdash; and the thank-you page names the <b>area code</b> that is about to call you.",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("Niche","Prop-firm trading"),("VSL","10m 35s"),("Words","2,378"),
           ("Streak claimed","862 days in a row"),("Rate claimed","7+ new traders/week"),
           ("CRM","GoHighLevel"),("Attribution","Hyros"),("Price","never stated")],
 "OFFER": [("Promise","&ldquo;Helping more than <b>7 new traders get their first payout every "
                      "single week</b> for over <b>862 days in a row</b>&rdquo;"),
   ("Problem named","&ldquo;Still stuck in the cycle of <b>strategy hopping &amp; emotional "
                    "trading</b>?&rdquo;"),
   ("Identity","&ldquo;Apply to see if you're a good fit to become a part of <b>the 1%</b>&rdquo;"),
   ("Path","Opt-in (name, email, phone) &rarr; VSL + Typeform application &rarr; thank-you"),
   ("Price","<b>Never stated.</b> Not on a page, not in the VSL")],
 "FINDINGS": [
  ("They name the area code that will call you &mdash; steal this",
   "The thank-you H1 is: <i>&ldquo;Wait, You're Not Done Yet! Our Team Will Be Calling You From A "
   "<b>+1 (305)</b> Phone Number ASAP To Walk You Through How To Get Onboarded.&rdquo;</i> "
   "Suprahuman warns that <i>an unknown number</i> will text. PB Trading goes one better and gives "
   "the actual area code, which turns an unknown caller into a recognised one. <b>This is the "
   "single cheapest speed-to-lead fix in the whole swipe file.</b>"),
  ("The proof is a streak, not a total",
   "&ldquo;862 days in a row&rdquo; and &ldquo;7 new traders every single week&rdquo;. A total "
   "(&ldquo;5,000 traders funded&rdquo;) is a claim about the past. <b>A streak is a claim about "
   "consistency, and it is falsifiable</b> &mdash; which is exactly why it reads as more honest. "
   "It also implies the result is systematic rather than lucky."),
  ("The enemy is a behaviour they already know they have",
   "&ldquo;Strategy hopping &amp; emotional trading&rdquo; is not a problem the copy has to teach "
   "&mdash; every failing trader recognises it instantly and is ashamed of it. The hook names the "
   "self-diagnosis rather than the outcome. Our equivalent is naming the loop, not the income."),
  ("Fifteen testimonial videos, all on the thank-you page",
   "None on the VSL page. The proof is spent <i>after</i> the application, on someone who has "
   "already committed &mdash; which is where doubt actually lives. Same instinct as Dlucs and "
   "Ecom Accelerator."),
 ],
 "FUNNEL": [
  ("Opt-in","pbtrading.io/join","Name, email, phone with country selector. Meta Pixel, GHL, Typeform, Hyros, Clarity."),
  ("VSL + application","pbtrading.io/video",'ConverteAI VSL, 10m35s. &ldquo;Apply to see if you are a good fit to become part of the 1%.&rdquo;'),
  ("Thank-you","pbtrading.io/thank-you",'<span class="tag good">the mechanic</span> Names the <b>+1 (305)</b> calling number. 2-minute what-happens-next video. 15 testimonial videos. FAQ.'),
 ],
 "TRANSCRIPT_GROUPS": [("PB Trading VSL",[os.path.join(PKG,"Transcript/transcript.md")])],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>Take the area code.</b> Three competitors in this file independently solved
&ldquo;the lead ignores our call&rdquo;. PB Trading's version is the most complete and takes one
line of copy on the confirmation page.</div>

<h2 class="sec">The unknown-number problem, solved three ways</h2>
<div class="tablewrap"><table>
<tr><th>Who</th><th>What they tell the lead</th><th>How strong</th></tr>
<tr><td>Suprahuman</td><td>&ldquo;An unknown number will text you within the hour &mdash; please reply&rdquo;</td><td>Sets expectation, asks for a micro-commitment</td></tr>
<tr><td>Brez Scales</td><td>&ldquo;Expect a text and a call in the next <b>2 minutes</b>&rdquo;</td><td>Sets a speed promise they must then hit</td></tr>
<tr><td><b>PB Trading</b></td><td>&ldquo;Our team will be calling from a <b>+1 (305)</b> number&rdquo;</td><td><b>Names the actual number pattern</b></td></tr>
</table></div>
<p style="margin-top:12px"><span class="tag">READ</span> We do none of these. Our booked leads get
a text and a call from numbers they have never seen, with no warning on any page. Three unrelated
markets independently concluded this was worth fixing.</p>

<h2 class="sec">Why &ldquo;862 days in a row&rdquo; works</h2>
<p>It is oddly specific, which reads as counted rather than rounded. It is a streak, so it implies
a system that has not broken. And it is <i>checkable in principle</i>, which is the quality that
separates a claim from a boast. Compare a competitor's &ldquo;3,000+ clients&rdquo; &mdash; larger,
and worth less.</p>
<p><span class="tag">READ</span> We have streak-shaped numbers we never use. Consecutive classes
run, consecutive weeks with a student win. Worth testing against our current totals-based proof.</p>

<h2 class="sec">The stack</h2>
<p>GoHighLevel + Typeform + <b>Hyros</b> + Meta Pixel + Clarity. Note the VSL page drops the Meta
Pixel that the opt-in page carries &mdash; conversions are attributed at the opt-in, and Hyros
carries the rest.</p>

<h2 class="sec">What is missing</h2>
<ul><li><b>No price</b> anywhere.</li>
<li><b>No emails</b> &mdash; opt-in never submitted.</li>
<li><b>The 15 thank-you testimonial videos are catalogued but not pulled.</b></li></ul>
""",
}
CONFIG["VIDEOS"] = video_library()

if __name__ == "__main__":
    build(CONFIG)
