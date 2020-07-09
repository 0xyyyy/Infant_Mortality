const url = {
    infant_url: "http://127.0.0.1:5000/api/v1.0/infants",
    birthweight_url: "http://127.0.0.1:5000/api/v1.0/birthweight",
    teen_url: "http://127.0.0.1:5000/api/v1.0/teen",
    unmarried_url: "http://127.0.0.1:5000/api/v1.0/unmarried",
    medianIncome_url: "http://127.0.0.1:5000/api/v1.0/medianincome",
    infant2018_url: "http://127.0.0.1:5000/api/v1.0/infants2018",
    birthweight2018_url: "http://127.0.0.1:5000/api/v1.0/birthweight2018",
    teen2018_url: "http://127.0.0.1:5000/api/v1.0/teen2018",
    unmarried2018_url: "http://127.0.0.1:5000/api/v1.0/unmarried2018"
}



// const infant_df = d3.json(url.infant_url).then(data => console.log(data));

//     const dataPromise_infant = d3.json(url.infant_url);
//     console.log("Data Promise: ", dataPromise_infant);

const infant2018_df = d3.json(url.infant2018_url).then(data=> console.log(data));

// const birthweight_df = d3.json(url.birthweight_url).then(data => console.log(data));

//     const dataPromise_birthweight = d3.json(url.infant_url);
//     console.log("Data Promise: ", dataPromise_birthweight);

const birthweight2018_df = d3.json(url.birthweight2018_url).then(data=> console.log(data));

// const teen_df = d3.json(url.teen_url).then(data => console.log(data));

//     const dataPromise_teen = d3.json(url.teen_url);
//     console.log("Data Promise: ", dataPromise_teen);

const teen2018_df = d3.json(url.teen2018_url).then(data=> console.log(data));

// const unmarried_df = d3.json(url.unmarried_url).then(data => console.log(data));

//     const dataPromise_unmarried = d3.json(url.unmarried_url);
//     console.log("Data Promise: ", dataPromise_unmarried);

const unmarried2018_df = d3.json(url.unmarried2018_url).then(data=> console.log(data))

const medianIncome_df = d3.json(url.medianIncome_url).then(data => console.log(data));

    const dataPromise_income = d3.json(url.medianIncome_url);
    console.log("Data Promsie: ", dataPromise_income);



