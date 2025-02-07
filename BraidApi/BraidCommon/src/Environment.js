"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ProductionEnvironment = exports.StagingEnvironment = exports.DevelopmentEnvironment = void 0;
/**
 * Class representing the Development Environment with methods to retrieve various API endpoints.
 * @class DevelopmentEnvironment
 */
class DevelopmentEnvironment {
    checkSessionApi() {
        return "http://localhost:7071/api/CheckSession";
    }
    summariseApi() {
        return "http://localhost:7071/api/Summarize";
    }
    classifyApi() {
        return "http://localhost:7071/api/Classify";
    }
    embedApi() {
        return "http://localhost:7071/api/Embed";
    }
    saveActivityApi() {
        return "http://localhost:7071/api/SaveActivity";
    }
    removeActivityApi() {
        return "http://localhost:7071/api/RemoveActivity";
    }
    getActivitiesApi() {
        return "http://localhost:7071/api/GetActivities";
    }
    loginWithLinkedInApi() {
        return "http://localhost:7071/api/LoginWithLinkedIn";
    }
    authFromLinkedInApi() {
        return "http://localhost:7071/api/ProcessAuthFromLinkedIn";
    }
    boxerHome() {
        return "http://localhost:1337/aibot.html";
    }
}
exports.DevelopmentEnvironment = DevelopmentEnvironment;
/**
 * Class representing the Staging Environment with methods to retrieve various API endpoints.
 * @class StagingEnvironment
 */
class StagingEnvironment {
    checkSessionApi() {
        return "https://braidapi.azurewebsites.net/api/CheckSession";
    }
    summariseApi() {
        return "https://braidapi.azurewebsites.net/api/Summarize";
    }
    classifyApi() {
        return "https://braidapi.azurewebsites.net/api/Classify";
    }
    embedApi() {
        return "https://braidapi.azurewebsites.net/api/Embed";
    }
    saveActivityApi() {
        return "https://braidapi.azurewebsites.net/api/SaveActivity";
    }
    removeActivityApi() {
        return "https://braidapi.azurewebsites.net/api/RemoveActivity";
    }
    getActivitiesApi() {
        return "https://braidapi.azurewebsites.net/api/GetActivities";
    }
    loginWithLinkedInApi() {
        return "https://braidapi.azurewebsites.net/api/LoginWithLinkedIn";
    }
    authFromLinkedInApi() {
        return "https://braidapi.azurewebsites.net/api/ProcessAuthFromLinkedIn";
    }
    boxerHome() {
        return "https://braidapps.io/aibot.html";
    }
}
exports.StagingEnvironment = StagingEnvironment;
/**
 * Class representing a Production Environment with methods to retrieve various API endpoints.
 * @class ProductionEnvironment
 */
class ProductionEnvironment {
    checkSessionApi() {
        return "https://braidapi.azurewebsites.net/api/CheckSession";
    }
    summariseApi() {
        return "https://braidapi.azurewebsites.net/api/Summarize";
    }
    classifyApi() {
        return "https://braidapi.azurewebsites.net/api/Classify";
    }
    embedApi() {
        return "https://braidapi.azurewebsites.net/api/Embed";
    }
    saveActivityApi() {
        return "https://braidapi.azurewebsites.net/api/SaveActivity";
    }
    removeActivityApi() {
        return "https://braidapi.azurewebsites.net/api/RemoveActivity";
    }
    getActivitiesApi() {
        return "https://braidapi.azurewebsites.net/api/GetActivities";
    }
    loginWithLinkedInApi() {
        return "https://braidapi.azurewebsites.net/api/LoginWithLinkedIn";
    }
    authFromLinkedInApi() {
        return "https://braidapi.azurewebsites.net/api/ProcessAuthFromLinkedIn";
    }
    boxerHome() {
        return "https://braidapps.io/aibot.html";
    }
}
exports.ProductionEnvironment = ProductionEnvironment;
//# sourceMappingURL=Environment.js.map