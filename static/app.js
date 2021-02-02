d3.csv("../data/albums_2020a.csv").then(albumsData =>
    {
        // console.log(albumsData)
        albumsData.forEach(row => {
            console.log(row.name);
        })
    });