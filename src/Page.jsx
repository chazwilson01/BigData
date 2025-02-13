import "./Page.css";

export default function ResourcesPage() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-6">Project Resources</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* HTML Data Links (Zipped) */}
        <div className="w-full p-4 text-center bg-white shadow-md rounded-lg">
          <div>
            <h2 className="text-xl font-semibold mb-2">HTML Data</h2>
            <a
              href="../public/tmdb_html_data.zip"
              download
              className="block bg-blue-500 text-white py-2 px-4 rounded mt-2"
            >
              Download TMDb HTML (ZIP)
            </a>
            <a
              href="../public/imdb_html_data.zip"
              download
              className="block bg-blue-500 text-white py-2 px-4 rounded mt-2"
            >
              Download IMDb HTML (ZIP)
            </a>
          </div>
        </div>

        {/* CSV Data Links */}
        <div className="w-full p-4 text-center bg-white shadow-md rounded-lg">
          <div>
            <h2 className="text-xl font-semibold mb-2">CSV Tables</h2>
            <a
              href="../public/tableA.csv"
              download
              className="block bg-green-500 text-white py-2 px-4 rounded mt-2"
            >
              Download Table A
            </a>
            <a
              href="../public/tableB.csv"
              download
              className="block bg-green-500 text-white py-2 px-4 rounded mt-2"
            >
              Download Table B
            </a>
          </div>
        </div>

        {/* Python Scripts */}
        <div className="w-full p-4 text-center bg-white shadow-md rounded-lg">
          <div>
            <h2 className="text-xl font-semibold mb-2">Scripts</h2>
            <a
              href="../public/tmdbScraper.py"
              download
              className="block bg-red-500 text-white py-2 px-4 rounded mt-2"
            >
              Download TMDb Scraper
            </a>
            <a
              href="../public/imdbScraper.py"
              download
              className="block bg-red-500 text-white py-2 px-4 rounded mt-2"
            >
              Download IMDb Scraper
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}