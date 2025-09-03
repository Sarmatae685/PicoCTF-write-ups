> [!NOTE]
> I wrote this note while solving [Torrent Analyze](../content/Forensics/Torrent%20Analyze.md) task.

<br/>

> [!TIP]
> Resources:
> - What are seeds, peers and leechers : [*click*](https://www.techworm.net/2017/03/seeds-peers-leechers-torrents-language.html)
> - Glossary of BitTorrent terms : [*click*](https://en.wikipedia.org/wiki/Glossary_of_BitTorrent_terms)
> - How Does BitTorrent Work? : [*click*](https://skerritt.blog/bit-torrent/)

### Leecher
**Leecher** - someone who downloads a file (parts of a file) and **does not yet have a complete copy** of the file. They can simultaneously download and distribute already downloaded parts to other peers.

In other words, a leech both downloads and distributes, but does not have 100% of the file.

---

### Seed
**Seed** - someone who has a complete copy of the file (100% downloaded) and **continues to distribute it** (uploaded, and did not delete it from downloads, and therefore SHARES it).  

A seed does not download anything, it only distributes.

---

### Peer
**Peer** - this is a general term for any participant in a BitTorrent swarm. A peer can be either a leech or a seed. In other words, anyone in the swarm who is both downloading and uploading is a peer.  

A leech is a specific type of peer who has not yet finished downloading. A seed is a specific type of peer who has already finished downloading and is only distributing.

---

### Understanding `sharing` term  
1. **Log in to the distribution server** : When you launch your BitTorrent client and download a torrent file, your client::  
   * Connects to a tracker (a server that coordinates distribution participants). The tracker does not store the file itself; it only knows which peers have which parts of the file.
   * Connects to other peers (participants) who are in the same swarm and are downloading/distributing the same file.
2. **You have become a "peer"** : From the moment your client connects to the swarm, you officially become a peer.
3. **While you are downloading the file (you are a "leecher")** :
   * You download pieces of the file from other seeds or leechers.
   * **At the same time** (and this is very important for BitTorrent), your client starts distributing the parts of the file that you have already successfully downloaded.
     
      That is, **you don't have to wait until you have downloaded everything 100% to start sharing**. This is what distinguishes BitTorrent from traditional centralized downloading.
   * **Yes, as long as you are online and a leech, other peers can download the parts you already have from you**.
4. When you have downloaded 100% of the file (you become a "seed"):
   * Once your BitTorrent client has downloaded **all the pieces of the file and assembled them into a complete file**, you **automatically become a seed**.
   * At this point, you are no longer downloading anything.
   * As long as you remain online on this server (i.e., your BitTorrent client is still active and distributing this torrent), other peers (leechers) can download this file from you.  

     You become the source of the complete file for them.

#### Summary
As soon as I enter the distribution server and automatically become a peer, while I am downloading the file in parts or have already downloaded it, as long as I am online on this server and am a peer (or a seed, when I have downloaded 100%), other peers can download the same thing as me.

---

### Torrent descriptor
**A torrent descriptor** is a small special file with the `.torrent` extension that contains metadata about the file you want to share, but **does not contain the file itself**.

#### What's inside a torrent file:

- File/folder name
- File size
- Size of the pieces into which the file is divided
- Cryptographic hashes of each piece (for integrity verification)
- Tracker address (coordinating server)
- Creation date and other service information

#### How it works
When you create a distribution, your BitTorrent client analyzes the original file, breaks it into pieces, calculates hashes, and creates this small `.torrent` file. **It is this descriptor** that you distribute through websites or transfer to other users.  

After creating the torrent file, you automatically *become the first seed* — the source of the complete copy of the file on the network. When other people download your `.torrent` file and open it in their client, *they become peers in the swarm* and start downloading the actual file.
Until they have downloaded the file completely, *they are leechers* - simultaneously downloading parts from you (the seed) and distributing the already downloaded parts to other peers. 
When one of them completes the download 100%, *they automatically become an additional seed*, increasing the number of sources of the complete file on the network.

---

### File "Health"
**Health** - is an indicator of how easily and quickly a particular torrent can be downloaded. Health depends on the **ratio of seeds to leechers** in the swarm.  

#### Indicators of a healthy torrent:

- Many seeds - there are several sources with a complete copy of the file.
- Active peers - users are online and actively distributing/downloading.
- Good ratio of seeds to leechers (for example, 5 seeds to 10 leechers).

#### Signs of an unhealthy torrent:

- Few or no seeds (especially critical when seeds = 0)
- Too many leechers with few seeds
- Inactive peers (have not been online for a long time)

#### Practical significance
A torrent with good health downloads quickly and stable. A torrent with poor health may download very slowly, stop at a certain percentage, or not download at all. 
Therefore, experienced users always check the seeds/leechers statistics before starting the download.
   
