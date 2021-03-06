import os
import shutil
import mosspy

def get_depth(path, depth=0):
    if not os.path.isdir(path): return depth
    maxdepth = depth
    for entry in os.listdir(path):
        fullpath = os.path.join(path, entry)
        maxdepth = max(maxdepth, get_depth(fullpath, depth + 1))
    return maxdepth


def run_moss():
    # swaxler
    # userid = 426819370
    # dropbox
    # userid = 796123625
    
    # shanewaxler1
    userid=428528030
    m = mosspy.Moss(userid, "python")

    path_to_moss = os.path.join(os.getcwd(),"moss")
    path_to_skeleton = os.path.join(path_to_moss, "skeleton")
    path_to_submissions = os.path.join(path_to_moss, "submissions")
    path_to_past_submissions = os.path.join(path_to_moss, "past-submissions")

    m.setDirectoryMode(1)

    m.setNumberOfMatchingFiles(200)

    m.addBaseFile("moss/skeleton/search.py")
    m.addBaseFile("moss/skeleton/searchAgents.py")
    m.addFilesByWildcard("moss/submissions/*/search*.py")
    m.addFilesByWildcard("moss/past-submissions/*/search*.py")
    
    s = "moss/past-submissions"
    e = "/search*.py"
    for _ in range(get_depth(path_to_past_submissions)):
        s += "/*"
        m.addFilesByWildcard(s+e)

    m.setIgnoreLimit(60)

    # print(len(m.files))
    # return 0    
    print("sending...")
    url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
    
    print()
    print("Report Url: " + url)


    """
    Uncomment the next three lines to save the entire report.
    """
    # os.makedirs(os.path.join(path_to_moss, "report"), exist_ok=True)
    # m.saveWebPage(url, "moss/report.html")
    # mosspy.download_report(url, "moss/searchpy-report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True))

    """
    Experimental:
    Uncomment this only if you've uncommented the last three lines.
    
    The code appends js to the end of the html file to exclude all
    percentages below "lowest_important_percentage".

    If you don't like what it did, just go into moss/report/index.html
    and remove the script.
    """
    # lowest_important_percentage = "10"
    # f = open("moss/report/index.html", "a")
    
    # f.write("""<script>
    # let rows = document.getElementsByTagName("tr");
    # let r = /\d+/;
    # let i = 1;
    # let removed;

    # while(rows[i]) {
    #     removed = false;
    #     for(let j = 0; j < 2; j++){
    #         if(parseInt(rows[i].children[j].innerText.match(r)[0]) < """ + lowest_important_percentage + """){
    #             rows[i].parentElement.removeChild(rows[i]);
    #             removed = true;
    #             break;
    #         }
    #     }
    #     if(!removed){
    #         i++;
    #     }
    # }
    # </script>""")
    # f.close()


if __name__ == "__main__":
    run_moss()
