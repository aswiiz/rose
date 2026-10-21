const giftItems=[
 {key:'hug',title:'A kitty hug',url:'https://giphy.com/embed/vxsoC27UotxBK',hint:'A little hug, just for you.',message:'A warm little kitty hug, just for you. If I could, I’d give you one right now. ♡'},
 {key:'flowers',title:'Flowers for you',url:'https://giphy.com/embed/5SbA6ZRhiI5jriUwqu',hint:'A tiny bouquet for my favorite person.',message:'A tiny bouquet to remind you that you make my days bloom. 💐'},
 {key:'chocolate',title:'Something sweet',url:'https://giphy.com/embed/V6L2QPnso9Jey5OH11',hint:'A sweet little surprise.',message:'Something sweet for someone who makes life sweeter. 🍫'},
 {key:'teddy',title:'A soft cuddle',url:'https://giphy.com/embed/o4M6gRwyyy6DC',hint:'A cozy cuddle whenever you need one.',message:'A soft virtual cuddle for whenever you need one. 🧸'},
 {key:'wish',title:'A little wish',url:'https://giphy.com/embed/nBKexBIYct2M9D6s1V',hint:'One little wish from my heart.',message:'A little wish: may we keep finding reasons to smile together. 💌'}
];
let giftIndex=0;
function renderGift(){
 const item=giftItems[giftIndex];
 const preview=document.getElementById('giftPreview');
 if(preview) preview.src=item.url;
 const title=document.getElementById('giftTitle'); if(title) title.textContent=item.title;
 const hint=document.getElementById('giftHint'); if(hint) hint.textContent=item.hint;
 const count=document.getElementById('giftCount'); if(count) count.textContent=`Gift ${giftIndex+1} of ${giftItems.length}`;
 const prev=document.getElementById('giftPrev'); if(prev) prev.disabled=giftIndex===0;
 const next=document.getElementById('giftNext'); if(next) next.disabled=giftIndex===giftItems.length-1;
 const reveal=document.getElementById('giftReveal'); if(reveal) reveal.hidden=true;
}
const prevGift=document.getElementById('giftPrev');
if(prevGift) prevGift.addEventListener('click',()=>{if(giftIndex>0){giftIndex--;renderGift();}});
const nextGift=document.getElementById('giftNext');
if(nextGift) nextGift.addEventListener('click',()=>{if(giftIndex<giftItems.length-1){giftIndex++;renderGift();}});
const openGift=document.getElementById('giftOpen');
if(openGift) openGift.addEventListener('click',()=>{
 const item=giftItems[giftIndex];
 const gif=document.getElementById('giftGif'); if(gif) gif.src=item.url;
 const message=document.getElementById('giftMessage'); if(message) message.textContent=item.message;
 const reveal=document.getElementById('giftReveal'); if(reveal) reveal.hidden=false;
});
const close=document.getElementById('closeGift');
if(close) close.addEventListener('click',()=>{
 const reveal=document.getElementById('giftReveal'); if(reveal) reveal.hidden=true;
});
const yes=document.getElementById('yesBtn');
if(yes) yes.addEventListener('click',()=>{
 const a=document.getElementById('answer');
 if(a) a.textContent='You made me so happy, Pavithra. Thank you for choosing to begin this with me. I’m looking forward to all the little memories we’ll make together. ❤️';
});
const time=document.getElementById('timeBtn');
if(time) time.addEventListener('click',()=>{
 const a=document.getElementById('answer');
 if(a) a.textContent='Of course, Pavithra. Take all the time you need. I care about you, and I want you to feel comfortable being honest with me. ❤️';
});
